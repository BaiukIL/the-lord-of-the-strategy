import pygame
from pygame_realization import camera, window, object_click_handler
from images import image
from configs import interface_config, game_config


class Interface:
    """
    Interface is a mediator (its coordinates windows work)
    which links interface windows together and coordinate its work.
    """

    camera: camera.Camera

    """
    A window which is located in the left bottom corner of the screen
    and responsible for showing selected object info.
    """
    selected: window.Window

    """
    A list of windows which are located in the middle bottom of the screen.
    Represents commands which selected object has.
    """
    commands: pygame.sprite.Group

    """
    A window which is located in the right bottom of the screen.
    Shows camera place at the map.
    """
    minimap: window.Window

    def __init__(self, world_map: pygame.Surface):
        self._map = world_map
        self.camera = camera.Camera(world_map.get_rect())
        self.commands = pygame.sprite.Group()

        self.selected = window.Window(interface_config.SELECTED_SIZE)
        self.selected.rect.bottomleft = (0, interface_config.SCR_HEIGHT)
        self.selected = window.add_borders(self.selected)
        self.selected.hide()

        self.minimap = window.Window(interface_config.MINIMAP_SIZE)
        self.minimap.image.blit(
            pygame.transform.scale(pygame.image.load(image.MAP), interface_config.MINIMAP_SIZE), (0, 0)
        )
        self.minimap.frame = pygame.transform.scale(
            pygame.image.load(image.MINIMAP_FRAME), interface_config.MINIMAP_FRAME_SIZE
        )
        self.minimap.rect.bottomright = interface_config.SCR_SIZE
        self.minimap.visible(200)

    def handle_object_click(self, args: (pygame.Surface, list, list)):
        self.selected.visible(170)

        image_handler = object_click_handler.ImageHandler(self.selected)
        text_handler = object_click_handler.TextHandler(self.selected)
        commands_handler = object_click_handler.CommandsHandler(
            start_pos=[self.selected.rect.right + interface_config.SELECTED_TO_COMMAND_INDENT,
                       interface_config.SCR_HEIGHT - interface_config.COMMAND_HEIGHT - 5],
            commands=self.commands
        )

        image_handler.set_next(text_handler).set_next(commands_handler)
        image_handler.handle(args)

    def handle_interface_click(self, mouse_pos: tuple):
        pass

    def handle_no_click(self):
        self.selected.hide()
        for command in self.commands:
            command.hide()

    def draw_windows(self, screen: pygame.Surface):
        # make place of camera location visible
        screen.blit(self._map, (-self.camera.x, -self.camera.y))
        # place `selected` in the left bottom corner
        screen.blit(self.selected.image, self.selected.rect.topleft)
        # draw commands in the middle bottom
        self.commands.draw(screen)
        # draw minimap in the right bottom corner
        self.minimap.image.blit(
            pygame.transform.scale(pygame.image.load(image.MAP), interface_config.MINIMAP_SIZE), (0, 0)
        )
        self.minimap.image.blit(
            self.minimap.frame,
            (int(self.camera.x * interface_config.MINIMAP_WIDTH / game_config.MAP_WIDTH),
             int(self.camera.y * interface_config.MINIMAP_HEIGHT / game_config.MAP_HEIGHT))
        )
        screen.blit(self.minimap.image, self.minimap.rect.topleft)
