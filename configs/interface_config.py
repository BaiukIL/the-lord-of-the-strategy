import pygame
from configs import game_config


SCR_SIZE = SCR_WIDTH, SCR_HEIGHT = 1920, 1000

CAMERA_START_POS = 0, 0
CAMERA_SPEED = 30

SELECTED_SIZE = SELECTED_WIDTH, SELECTED_HEIGHT = 200, 200
SELECTED_TO_COMMAND_INDENT = 100

COMMAND_SIZE = COMMAND_WIDTH, COMMAND_HEIGHT = 80, 80
COMMANDS_INDENT = 130

MINIMAP_WIDTH = 400
MINIMAP_HEIGHT = int(MINIMAP_WIDTH * game_config.MAP_HEIGHT / game_config.MAP_WIDTH)
MINIMAP_SIZE = MINIMAP_WIDTH, MINIMAP_HEIGHT

BORDERS_COLOR = pygame.Color(255, 255, 0)
BORDERS_SIZE = 2
