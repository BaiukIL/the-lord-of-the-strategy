import pygame
from pygame_realization import base_handler, window
from configs import game_config, interface_config
from abc import ABC


class SelectedHandler(base_handler.BaseHandler, ABC):
    def __init__(self, selected: window.Window):
        self._selected = selected


class ImageHandler(SelectedHandler):
    """Place image onto surface"""
    def _handle(self, args):
        image = args[0]
        surface = pygame.transform.scale(
            image,
            (interface_config.SELECTED_HEIGHT // 2, interface_config.SELECTED_WIDTH // 2)
        )
        self._selected.blit(surface, (0, interface_config.SELECTED_WIDTH // 2))


class TextHandler(SelectedHandler):
    """Write text onto surface"""
    def _handle(self, args):
        text = args[0]
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 20
        # `5` is indent from left screen side
        line_pos = [5, 0]
        for line in text:
            self._selected.blit(font.render(line, True, game_config.WHITE), line_pos)
            line_pos[1] += indent


class CommandsHandler(base_handler.BaseHandler):
    def __init__(self, start_pos: list, commands: list):
        self.pos = start_pos
        self.commands = commands

    def _handle(self, args):
        commands = args[0]
        self.commands.clear()

        for command in commands:
            message, action, image_file = command
            image_surf = pygame.transform.scale(pygame.image.load(image_file), interface_config.COMMAND_SIZE)
            command_window = window.Window(interface_config.COMMAND_SIZE, message=message, visible=True)
            command_window.blit(image_surf, (0, 0))
            command_window.rect.topleft = self.pos
            self.commands.append(command_window)

            self.pos[0] += interface_config.COMMANDS_INDENT
