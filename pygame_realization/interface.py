import pygame
from pygame_realization import window, singleton, map
from configs import interface_config, game_config


class Camera(pygame.Rect, metaclass=singleton.Singleton):
    """
    It is a frame within which player can see game changes
    """
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

    # Check map borders collision
    def _fix_collision_with_map(self):
        if self.left < 0:
            self.left = 0
        elif self.right > map.Map().rect.right:
            self.right = map.Map().rect.right
        if self.bottom > map.Map().rect.bottom:
            self.bottom = map.Map().rect.bottom
        elif self.top < 0:
            self.top = 0


class Selected(window.Window, metaclass=singleton.Singleton):
    """
    A window which is located in the left bottom corner of the screen
    and responsible for showing selected object info.
    """

    def __init__(self):
        window.Window.__init__(self, interface_config.SELECTED_SIZE)
        self.rect.bottomleft = (0, interface_config.SCR_HEIGHT)
        self.add_borders()
        self.hide()

    def place_text(self, text: str):
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 20
        # interface_config.BORDERS_SIZE is indent from left side of selected screen
        line_pos = [interface_config.BORDERS_SIZE, 0]
        for line in text.split('\n'):
            self.image.blit(font.render(line, True, pygame.Color('white')), line_pos)
            line_pos[1] += indent

    def place_image(self, image: pygame.Surface):
        self.image.blit(
            pygame.transform.scale(image, (interface_config.SELECTED_WIDTH // 2,
                                           interface_config.SELECTED_HEIGHT // 2)),
            (0, interface_config.SELECTED_HEIGHT // 2))


class Minimap(window.Window, metaclass=singleton.Singleton):
    """
    A window which is located in the right bottom of the screen.
    Shows camera place at the map.
    """

    _frame: pygame.Rect

    def __init__(self):
        window.Window.__init__(self, interface_config.MINIMAP_SIZE)
        self.image = pygame.transform.scale(map.Map().image, interface_config.MINIMAP_SIZE)
        self.rect.bottomright = interface_config.SCR_SIZE
        self.active(200)
        self.add_borders()

        self._frame = pygame.Rect(self.rect.topleft, interface_config.MINIMAP_FRAME_SIZE)

    def move_frame(self, pos: tuple):
        self._frame.x = int(pos[0] * interface_config.MINIMAP_WIDTH / game_config.MAP_WIDTH)
        self._frame.y = int(pos[1] * interface_config.MINIMAP_HEIGHT / game_config.MAP_HEIGHT)

    def sync_with_map(self):
        self.image = pygame.transform.scale(map.Map().image, interface_config.MINIMAP_SIZE)
        pygame.draw.rect(self.image, interface_config.BORDERS_COLOR, self._frame, 1)


class Command(window.Window):
    """
    A window which is located in the middle bottom of the screen.
    Represents commands which selected object has.
    """
    pass


class Interface(metaclass=singleton.Singleton):
    """
    Interface is a mediator which links interface windows together
    and coordinate its work.
    """

    commands: pygame.sprite.Group

    def __init__(self):
        self.commands = pygame.sprite.Group()

    def move_view(self, key, mouse_pos):
        Camera().move_view(key, mouse_pos)
        Minimap().move_frame(Camera().topleft)

    def _place_commands(self, commands):
        self.commands.empty()
        pos = [Selected().rect.right + interface_config.SELECTED_TO_COMMAND_INDENT,
               interface_config.SCR_HEIGHT - interface_config.COMMAND_HEIGHT - 10]
        for command in commands:
            message, action, image_file = command
            image_surf = pygame.transform.scale(pygame.image.load(image_file), interface_config.COMMAND_SIZE)
            command_window = window.Window(interface_config.COMMAND_SIZE)
            command_window.hint_message = message
            command_window.image = image_surf
            command_window.rect.topleft = pos
            pos[0] += interface_config.COMMANDS_INDENT
            self.commands.add(command_window)

    def handle_object_click(self, args: (pygame.Surface, str, list)):
        Selected().active(170)
        image, text, commands = args
        Selected().reset()
        Selected().place_image(image)
        Selected().place_text(text)
        self._place_commands(commands)

    def handle_no_click(self):
        Selected().hide()
        for command in self.commands:
            command.hide()

    def draw_windows(self, screen: pygame.Surface):
        # make place of camera location visible
        screen.blit(map.Map().image, (-Camera().x, -Camera().y))
        screen.blit(Selected().image, Selected().rect.topleft)
        Minimap().sync_with_map()
        screen.blit(Minimap().image, Minimap().rect.topleft)
        self.commands.draw(screen)
