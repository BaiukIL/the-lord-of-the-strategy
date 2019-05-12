import pygame
from interface import window, button
import map
import configs
import templates
from typing import *


def get_global_mouse_pos(mouse_pos: Tuple[int, int]) -> Tuple[int, int]:
    """Mouse position with a glance to camera position on the map"""
    return mouse_pos[0] + Interface().camera.x, mouse_pos[1] + Interface().camera.y


class Camera(pygame.Rect):
    """It is a frame within which player can see game changes"""

    def __init__(self):
        super().__init__(configs.CAMERA_START_POS, configs.SCR_SIZE)
        self._speed = configs.CAMERA_SPEED

    def move_view(self, key, mouse_pos: Tuple[int, int]):
        if key[pygame.K_w] or mouse_pos[1] == 0:
            self.y -= self._speed
        if key[pygame.K_s] or mouse_pos[1] == configs.SCR_HEIGHT - 1:
            self.y += self._speed
        if key[pygame.K_a] or mouse_pos[0] == 0:
            self.x -= self._speed
        if key[pygame.K_d] or mouse_pos[0] == configs.SCR_WIDTH - 1:
            self.x += self._speed
        self._fix_collision_with_map()

    def _fix_collision_with_map(self):
        """Check map borders collision"""
        if self.left < 0:
            self.left = 0
        elif self.right > map.Map().rect.right:
            self.right = map.Map().rect.right
        if self.bottom > map.Map().rect.bottom:
            self.bottom = map.Map().rect.bottom
        elif self.top < 0:
            self.top = 0


class Selected(window.Window):
    """A window which is located in the left bottom corner of the screen
    and responsible for showing selected object info."""

    def __init__(self):
        window.Window.__init__(self, configs.SELECTED_SIZE)
        self.rect.bottomleft = (0, configs.SCR_HEIGHT)
        self.text = str()
        self.set_default_alpha(170)
        self.set_never_bordered()
        self.hide()

    def hide(self):
        self.clear()
        self.change_state(window.HiddenWindowState(self))

    def select_object(self, obj):
        self.clear()
        self.active()
        self._place_object_image(obj.real_image)
        self._place_object_text(obj.info())
        self._show_empire_info(obj.empire)

    def _show_empire_info(self, empire):
        pass

    def _place_object_image(self, image: pygame.Surface):
        selected_img_side_size = min(self.rect.width // 2, self.rect.height // 2)
        self.real_image.blit(pygame.transform.scale(image, (selected_img_side_size,
                                                            selected_img_side_size)),
                             (self.rect.width // 2, self.rect.height // 2))

    def _place_object_text(self, text: Text):
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 25
        # interface_config.BORDERS_SIZE is indent from left side of selected screen
        line_pos = [0, 0]
        for line in text.split('\n'):
            self.real_image.blit(font.render(line, True, (0, 0, 0)), line_pos)
            line_pos[1] += indent


class Minimap(window.Window):
    """A window which is located in the right bottom of the screen.
    Shows camera place at the map."""

    _frame: pygame.Rect

    def __init__(self):
        window.Window.__init__(self, configs.MINIMAP_SIZE, image=map.Map().image)
        self.rect.bottomright = configs.SCR_SIZE
        self.set_constant_bordered()
        self.set_default_alpha(170)

        self._frame = pygame.Rect(
            self.rect.topleft, (
                int(self.rect.width * configs.SCR_WIDTH / map.Map().rect.width),
                int(self.rect.height * configs.SCR_HEIGHT / map.Map().rect.height)))

    def move_frame(self, pos: tuple):
        self._frame.x = int(pos[0] * self.rect.width / map.Map().rect.width)
        self._frame.y = int(pos[1] * self.rect.height / map.Map().rect.height)

    def action_while_update(self):
        self.clear()
        self.real_image.blit(pygame.transform.scale(map.Map().image, self.rect.size), (0, 0))
        pygame.draw.rect(self.real_image, self._borders_color, self._frame, 1)


class EmpireInfo:
    def __init__(self, empire, enemy: bool):
        self.empire = empire
        self.empire_icon = window.Window(size=(100, 100), image=empire.icon)
        self.empire_icon.set_default_alpha(170)
        self.resources = window.Window((220, 50))
        self.resources.set_default_alpha(170)
        if enemy:
            self.empire_icon.rect.topright = configs.SCR_WIDTH, 0
            self.resources.rect.topright = configs.SCR_WIDTH, 120
        else:
            self.empire_icon.rect.topleft = 0, 0
            self.resources.rect.topleft = 0, 120

    def update(self):
        font = pygame.font.SysFont(name='Ani', size=30)
        self.resources.clear()
        self.resources.real_image.blit(
            font.render('Resources: {}'.format(self.empire.resources), True, pygame.Color('black')), (0, 0))

    def draw(self, screen: pygame.Surface):
        screen.blit(self.empire_icon.real_image, self.empire_icon.rect)
        screen.blit(self.resources.real_image, self.resources.rect)


class Interface(templates.Handler, metaclass=templates.Singleton):
    """Interface is a mediator which coordinates interface windows work."""

    def __init__(self, player_empire, enemy_empire):
        self.player_empire = player_empire
        self.camera = Camera()
        self.selected = Selected()
        self.minimap = Minimap()
        self.commands = pygame.sprite.Group()
        self.messages = pygame.sprite.Group()
        self.player_empire_info = EmpireInfo(player_empire, enemy=False)
        self.enemy_empire_info = EmpireInfo(enemy_empire, enemy=True)
        # The most recent chosen (selected) game object
        # and command respectively
        self.buffer = pygame.sprite.GroupSingle()
        self.command = pygame.sprite.GroupSingle()

    def hide_all(self):
        self.commands.empty()
        self.selected.hide()
        self.change_selected_object(None)
        self.change_selected_command(None)

    def change_selected_object(self, obj):
        for buffered in self.buffer:
            buffered.passive()
        self.buffer.empty()
        if obj is not None:
            self.buffer.add(obj)

    def change_selected_command(self, command: button.Button or None):
        for com in self.command:
            com.passive()
        self.command.empty()
        if command is not None:
            self.command.add(command)

    def move_view(self, key, mouse_pos: Tuple[int, int]):
        self.camera.move_view(key, mouse_pos)
        self.minimap.move_frame(self.camera.topleft)

    def handle_click(self, mouse_pos: Tuple[int, int]):
        for command in self.commands:
            if command.handle_click(mouse_pos):
                return True
        if self.selected.handle_click(mouse_pos):
            return True
        if self.minimap.handle_click(mouse_pos):
            return True
        return False

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        # Check if selected object can handle empty click
        for buffered in self.buffer:
            buffered.handle_empty_click(get_global_mouse_pos(mouse_pos))
        # If command is activated and can handle empty click, it'll be executed
        for com in self.command:
            if com.activated:
                com.handle_empty_click(get_global_mouse_pos(mouse_pos))
        self.hide_all()

    def handle_object_click(self, obj):
        for buffered in self.buffer:
            buffered.handle_object_click(obj)
        for com in self.command:
            if com.activated:
                com.handle_object_click(obj)
        self.change_selected_object(obj)
        self.change_selected_command(None)
        self.selected.select_object(obj)
        self.commands.empty()
        # if given object belongs to player's empire,
        # let work with it. Otherwise do not show commands
        if obj.empire is self.player_empire:
            self._place_commands(obj)

    def draw_interface(self, screen: pygame.Surface):
        # make place of camera location visible
        screen.blit(map.Map().image, (-self.camera.x, -self.camera.y))
        # draw interface windows
        self.selected.update()
        screen.blit(self.selected.image, self.selected.rect)
        self.minimap.update()
        screen.blit(self.minimap.image, self.minimap.rect)
        self.messages.update()
        self.messages.draw(screen)
        self.commands.draw(screen)
        self.player_empire_info.update()
        self.player_empire_info.draw(screen)
        self.enemy_empire_info.update()
        self.enemy_empire_info.draw(screen)

    def _place_commands(self, obj):
        pos = [self.selected.rect.right + configs.SELECTED_TO_COMMAND_INDENT,
               configs.SCR_HEIGHT - configs.COMMAND_HEIGHT - 10]

        for command in obj.mouse_interaction_commands:
            command_window = button.MouseInteractionButton(*command, interface=self)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += configs.COMMANDS_INDENT

        for command in obj.no_interaction_commands:
            command_window = button.NoInteractionButton(*command, interface=self)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += configs.COMMANDS_INDENT

        for command in obj.object_interaction_commands:
            command_window = button.ObjectInteractionButton(*command, interface=self)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += configs.COMMANDS_INDENT
