import pygame
from interface import window
import map
from configs import interface_config
import templates
from typing import *


def get_global_mouse_pos(mouse_pos: Tuple[int, int]) -> Tuple[int, int]:
    """Mouse position with a glance to camera position on the map"""
    return mouse_pos[0] + Interface().camera.x, mouse_pos[1] + Interface().camera.y


class Camera(pygame.Rect):
    """It is a frame within which player can see game changes"""

    def __init__(self):
        super().__init__(interface_config.CAMERA_START_POS, interface_config.SCR_SIZE)
        self._speed = interface_config.CAMERA_SPEED

    def move_view(self, key, mouse_pos: Tuple[int, int]):
        if key[pygame.K_w] or mouse_pos[1] == 0:
            self.y -= self._speed
        if key[pygame.K_s] or mouse_pos[1] == interface_config.SCR_HEIGHT - 1:
            self.y += self._speed
        if key[pygame.K_a] or mouse_pos[0] == 0:
            self.x -= self._speed
        if key[pygame.K_d] or mouse_pos[0] == interface_config.SCR_WIDTH - 1:
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
        window.Window.__init__(self, interface_config.SELECTED_SIZE)
        self.rect.bottomleft = (0, interface_config.SCR_HEIGHT)
        self.set_default_alpha(170)
        self.set_never_bordered()
        self.hide()

    def hide(self):
        self.clear()
        self.change_state(window.HiddenWindowState(self))

    def select_object(self, obj):
        self.clear()
        self.active()
        self._place_image(obj._image)
        self._place_text(obj.info())

    def _place_image(self, image: pygame.Surface):
        selected_img_side_size = min(self.rect.width // 2, self.rect.height // 2)
        self._image.blit(pygame.transform.scale(image, (selected_img_side_size,
                                                        selected_img_side_size)),
                         (self.rect.width // 2, self.rect.height // 2))

    def _place_text(self, text: Text):
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 25
        # interface_config.BORDERS_SIZE is indent from left side of selected screen
        line_pos = [0, 0]
        for line in text.split('\n'):
            self._image.blit(font.render(line, True, interface_config.SELECTED_TEXT_COLOR), line_pos)
            line_pos[1] += indent


class Minimap(window.Window):
    """A window which is located in the right bottom of the screen.
    Shows camera place at the map."""

    _frame: pygame.Rect

    def __init__(self):
        window.Window.__init__(self, interface_config.MINIMAP_SIZE, image=map.Map().image)
        self.rect.bottomright = interface_config.SCR_SIZE
        self.set_constant_bordered()
        self.set_default_alpha(170)

        self._frame = pygame.Rect(
            self.rect.topleft, (
                int(self.rect.width * interface_config.SCR_WIDTH / map.Map().rect.width),
                int(self.rect.height * interface_config.SCR_HEIGHT / map.Map().rect.height)))

    def move_frame(self, pos: tuple):
        self._frame.x = int(pos[0] * self.rect.width / map.Map().rect.width)
        self._frame.y = int(pos[1] * self.rect.height / map.Map().rect.height)

    def update(self):
        self.clear()
        self._image.blit(pygame.transform.scale(map.Map().image, self.rect.size), (0, 0))
        pygame.draw.rect(self._image, self._borders_color, self._frame, 1)


class Command(window.Window):
    """A window which is located in the middle bottom of the screen.
    Represents commands which selected object has."""

    _action: Callable
    activated: bool = False

    def __init__(self, image: pygame.Surface, action: Callable, message: Text):
        window.Window.__init__(self, interface_config.COMMAND_SIZE, image)
        self._action = action
        self._hint_message = message

    def active(self):
        self.change_state(window.ActiveWindowState(self))
        self.activated = True

    def passive(self):
        self.change_state(window.PassiveWindowState(self))
        self.activated = False

    def click_action(self):
        Interface().change_selected_command(self)

    def return_click_action(self):
        Interface().change_selected_command(None)

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        pass

    def handle_object_click(self, obj):
        pass

    def execute(self, *args):
        self._action(*args)
        self.passive()


class NoInteractionCommand(Command):
    def click_action(self):
        Interface().change_selected_command(self)
        self.execute()


class MouseInteractionCommand(Command):
    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        self.execute(mouse_pos)


class ObjectInteractionCommand(Command):
    def handle_object_click(self, obj):
        self.execute(obj)


class Interface(templates.Handler, metaclass=templates.Singleton):
    """Interface is a mediator which coordinates interface windows work."""

    def __init__(self, player):
        self.player = player
        self.camera = Camera()
        self.selected = Selected()
        self.minimap = Minimap()
        self.commands = pygame.sprite.Group()
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

    def change_selected_command(self, command: 'Command' or None):
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
        if obj.empire is self.player.empire:
            self._place_commands(obj)

    def draw_interface(self, screen: pygame.Surface):
        # make place of camera location visible
        screen.blit(map.Map().image, (-self.camera.x, -self.camera.y))
        # draw interface windows
        self.selected.update()
        screen.blit(self.selected.image, self.selected.rect)
        self.minimap.update()
        screen.blit(self.minimap.image, self.minimap.rect)
        self.commands.draw(screen)

    def _place_commands(self, obj):
        pos = [self.selected.rect.right + interface_config.SELECTED_TO_COMMAND_INDENT,
               interface_config.SCR_HEIGHT - interface_config.COMMAND_HEIGHT - 10]

        for command in obj.mouse_interaction_commands:
            command_window = MouseInteractionCommand(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += interface_config.COMMANDS_INDENT

        for command in obj.no_interaction_commands:
            command_window = NoInteractionCommand(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += interface_config.COMMANDS_INDENT

        for command in obj.object_interaction_commands:
            command_window = ObjectInteractionCommand(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += interface_config.COMMANDS_INDENT
