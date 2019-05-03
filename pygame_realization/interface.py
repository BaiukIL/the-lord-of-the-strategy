import pygame
from pygame_realization import camera, window, object_click_handler
from configs import interface_config


# Mediator
class Interface:
    """
    Interface is a mediator (its coordinates windows work)
    which links camera and windows together.
    """
    camera: camera.Camera

    """
    A window which is located in the left bottom corner of the screen
    and responsible for showing selected object info.
    """
    selected: window.Window

    """
    List of windows, located in the middle bottom of the screen.
    Represents commands which selected object has
    """
    commands: list

    def __init__(self, world_map: pygame.Surface):
        self._map = world_map
        self.camera = camera.Camera(world_map)
        self.selected = window.Window(interface_config.SELECTED_SIZE)
        self.selected.hide()
        self.commands = list()

    def handle_object_click(self, args: (pygame.Surface, list, list)):
        self.selected.visible()

        image_handler = object_click_handler.ImageHandler(self.selected)
        text_handler = object_click_handler.TextHandler(self.selected)
        commands_handler = object_click_handler.CommandsHandler(
            start_pos=[self.selected.rect.right + interface_config.SELECTED_COMMAND_INDENT,
                       interface_config.SCR_HEIGHT - interface_config.COMMAND_HEIGHT - 5],
            commands=self.commands
        )

        image_handler.set_next(text_handler).set_next(commands_handler)
        image_handler.handle(args)

    def handle_no_click(self):
        self.selected.hide()
        for command in self.commands:
            command.hide()

    def draw_windows(self, screen: pygame.Surface):
        surface_rect = screen.get_rect()
        # make place of camera location visible
        screen.blit(self._map, (-self.camera.x, -self.camera.y))
        # place `selected` in left bottom corner
        screen.blit(self.selected, (surface_rect.left, surface_rect.bottom - self.selected.get_rect().height))

        for command in self.commands:
            screen.blit(command, command.rect.topleft)
