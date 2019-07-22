""" This module contains interface settings.
Mostly there are windows sizes, start coordinates and colors.
Do not change if not confident. """


import game_configs


SCR_SIZE = SCR_WIDTH, SCR_HEIGHT = game_configs.SCR_SIZE

CAMERA_START_POS = 0, game_configs.MAP_HEIGHT // 2 - 400
CAMERA_SPEED = 30

MINIMAP_WIDTH = 400
MINIMAP_HEIGHT = MINIMAP_WIDTH * game_configs.MAP_HEIGHT // game_configs.MAP_WIDTH
MINIMAP_SIZE = MINIMAP_WIDTH, MINIMAP_HEIGHT

COMMAND_SIZE = COMMAND_WIDTH, COMMAND_HEIGHT = 80, 80
# Indent between commands.
COMMANDS_INDENT = 130

SELECTED_SIZE = SELECTED_WIDTH, SELECTED_HEIGHT = 250, 250
SELECTED_TEXT_COLOR = 255, 255, 255
# Indent between selected object info and first command.
SELECTED_TO_COMMAND_INDENT = 100

BORDERS_COLOR = 100, 100, 100
BORDERS_SIZE = 1

FONT_STYLE = 'AnjaliOldLipi'
FONT_SIZE = 20
# Vertical indent between lines.
VERTICAL_LINES_INDENT = 20
