import pygame
from interface import window
from game_objects import map
from configs import interface_config
import templates
from typing import *


class Camera(pygame.Rect):
    """It is a frame within which player can see game changes"""

    def __init__(self):
        super().__init__(interface_config.CAMERA_START_POS, interface_config.SCR_SIZE)
        self._speed = interface_config.CAMERA_SPEED

    def move_view(self, key, mouse_pos):
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

    """The most recent chosen (selected) game object"""
    buffer: window.Window = None

    def __init__(self):
        window.Window.__init__(self, interface_config.SELECTED_SIZE)
        self.rect.bottomleft = (0, interface_config.SCR_HEIGHT)
        self.add_borders()
        self.hide()

    def handle_object_click(self, obj):
        # self.reset()
        self.buffer = obj
        self._place_image(obj.inner_image)
        self._place_text(obj.info())
        self.active(170)

    def handle_no_click(self):
        self.buffer.active(self.buffer.image.get_alpha())
        self.buffer.remove_borders()
        self.hide()

    def _place_image(self, image: pygame.Surface):
        self.inner_image.blit(
            pygame.transform.scale(image, (self.inner_image.get_width() // 2,
                                           self.inner_image.get_height() // 2)),
            (0, self.inner_image.get_height() // 2))

    def _place_text(self, text: str):
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 20
        # interface_config.BORDERS_SIZE is indent from left side of selected screen
        line_pos = [0, 0]
        for line in text.split('\n'):
            self.inner_image.blit(font.render(line, True, pygame.Color('white')), line_pos)
            line_pos[1] += indent


class Minimap(window.Window):
    """A window which is located in the right bottom of the screen.
    Shows camera place at the map."""

    _frame: pygame.Rect

    def __init__(self):
        window.Window.__init__(self, interface_config.MINIMAP_SIZE, image=map.Map().image)
        self.rect.bottomright = interface_config.SCR_SIZE
        self.active(200)
        self.add_borders()

        self._frame = pygame.Rect(
            self.rect.topleft, (
                int(self.inner_image.get_width() * interface_config.SCR_WIDTH / map.Map().rect.width),
                int(self.inner_image.get_height() * interface_config.SCR_HEIGHT / map.Map().rect.height)))

    def move_frame(self, pos: tuple):
        self._frame.x = int(pos[0] * self.inner_image.get_width() / map.Map().rect.width)
        self._frame.y = int(pos[1] * self.inner_image.get_height() / map.Map().rect.height)

    def update(self):
        self.inner_image.blit(pygame.transform.scale(map.Map().image, self.inner_image.get_size()), (0, 0))
        pygame.draw.rect(self.inner_image, self.borders_color, self._frame, 1)


class Command(window.Window):
    """A window which is located in the middle bottom of the screen.
    Represents commands which selected object has."""

    _action: Callable

    def __init__(self, image_file: str, action: Callable, message: Text):
        window.Window.__init__(self, interface_config.COMMAND_SIZE, pygame.image.load(image_file))
        self._action = action
        self._hint_message = message
        self.add_borders()

    def handle(self, mouse_pos: Tuple[int, int]):
        pass


class Interface(templates.Handler, templates.Subscriber, metaclass=templates.Singleton):
    """Interface is a mediator which coordinates interface windows work."""

    camera: Camera
    selected: Selected
    minimap: Minimap
    commands: pygame.sprite.Group

    def __init__(self):
        self.camera = Camera()
        self.selected = Selected()
        self.minimap = Minimap()
        self.commands = pygame.sprite.Group()

    def move_view(self, key, mouse_pos: Tuple[int, int]):
        self.camera.move_view(key, mouse_pos)
        self.minimap.move_frame(self.camera.topleft)

    def handle_click(self, mouse_pos: Tuple[int, int]):
        for command in self.commands:
            if command.handle_click(mouse_pos):
                return True
        return self.selected.handle_click(mouse_pos) and self.minimap.handle_click(mouse_pos)

    def handle_object_click(self, obj):
        self.selected.handle_object_click(obj)
        self._place_commands(obj)

    def handle_no_click(self):
        self.commands.empty()
        self.selected.handle_no_click()

    def draw_interface(self, screen: pygame.Surface):
        # make place of camera location visible
        screen.blit(map.Map().image, (-self.camera.x, -self.camera.y))
        # draw interface windows
        screen.blit(self.selected.image, self.selected.rect)
        self.minimap.update()
        screen.blit(self.minimap.image, self.minimap.rect)
        self.commands.draw(screen)

    def _place_commands(self, obj):
        self.commands.empty()
        pos = [self.selected.rect.right + interface_config.SELECTED_TO_COMMAND_INDENT,
               interface_config.SCR_HEIGHT - interface_config.COMMAND_HEIGHT - 10]
        for command in obj.commands:
            command_window = Command(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += interface_config.COMMANDS_INDENT
