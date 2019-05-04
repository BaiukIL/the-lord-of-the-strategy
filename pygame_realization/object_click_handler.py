import pygame
from pygame_realization import base_handler, window
from configs import game_config, interface_config
from abc import ABC


class SelectedHandler(base_handler.BaseHandler, ABC):
    def __init__(self, selected: window.Window):
        self._selected = selected


class ImageHandler(SelectedHandler):
    """Place selected image"""
    def _handle(self, args):
        selected_image = args[0]
        surface = pygame.transform.scale(
            selected_image,
            (interface_config.SELECTED_WIDTH // 2 - interface_config.BORDERS_SIZE,
             interface_config.SELECTED_HEIGHT // 2 - interface_config.BORDERS_SIZE)
        )
        self._selected.image.blit(surface, (interface_config.BORDERS_SIZE,
                                            interface_config.SELECTED_WIDTH // 2))


class TextHandler(SelectedHandler):
    """Write text onto surface"""
    def _handle(self, args):
        text = args[0]
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 20
        # interface_config.BORDERS_SIZE is indent from left side of selected screen
        line_pos = [interface_config.BORDERS_SIZE, 0]
        for line in text:
            self._selected.image.blit(font.render(line, True, game_config.WHITE), line_pos)
            line_pos[1] += indent


class CommandsHandler(base_handler.BaseHandler):
    def __init__(self, start_pos: list, commands: pygame.sprite.Group):
        self.pos = start_pos
        self.commands = commands

    def _handle(self, args):
        commands = args[0]
        self.commands.empty()

        for command in commands:
            message, action, image_file = command
            image_surf = pygame.transform.scale(pygame.image.load(image_file), interface_config.COMMAND_SIZE)
            command_window = window.Window(interface_config.COMMAND_SIZE, message=message)
            command_window.image.blit(image_surf, (0, 0))
            command_window.rect.topleft = self.pos
            self.commands.add(command_window)

            self.pos[0] += interface_config.COMMANDS_INDENT
