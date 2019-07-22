"""This script is executed with 'stress_test_statistic', which is located
in root project directory because it's impossible to import upper level modules"""


import pygame
# project modules #
from game import Game
from game_objects import empire, races, world_map
from tests.stress_tests.stress_AI import StressAI
from interface.interface import Interface, get_global_mouse_pos
import configs
import user_configs
import image as img


def clear_callback(surf, rect):
    surf.fill(world_map.Map().color, rect)


def play_game():
    # pygame initialization start
    pygame.init()
    screen = pygame.display.set_mode(configs.SCR_SIZE)
    pygame.display.set_caption("the Lord of the Strategy")
    icon_surf = img.get_image().ICON
    pygame.display.set_icon(icon_surf)
    clock = pygame.time.Clock()

    if not pygame.font.get_init():
        raise SystemExit("Fonts are out-of-service")
    # pygame initialization finish

    # game objects initialization start
    player_empire = empire.Empire(user_configs.EMPIRE_RACE, name=user_configs.EMPIRE_NAME, start_resources=1000)
    enemy_empire = empire.Empire(races.DWARFS, name='Durden', start_resources=1000)

    game = Game(player_empire, enemy_empire)
    interface = Interface(player_empire, enemy_empire)

    player_empire.set_city("Nevborn")
    player_default_city = player_empire.get_city("Nevborn")
    player_default_city.rect.x = 500
    player_default_city.rect.centery = world_map.Map().rect.centery

    enemy_empire.set_city("Nuhen")
    enemy_default_city = enemy_empire.get_city("Nuhen")
    enemy_default_city.rect.right = world_map.Map().rect.right - 700
    enemy_default_city.rect.centery = world_map.Map().rect.centery
    StressAI(enemy_empire)
    # game objects initialization start

    rendered = None
    while True:
        mouse_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

        key = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pressed:
            handled = False
            # check if any of interface windows can handle click
            if interface.handle_interface_click(mouse_pos):
                handled = True
            else:
                for obj in game.objects:
                    # check if any of game objects can handle click
                    if obj.handle_click(get_global_mouse_pos(mouse_pos)):
                        handled = True
            if not handled:
                interface.handle_empty_click(mouse_pos)

        # AI is singleton, which has initialized before
        StressAI().play_step()

        # If any of empires is out of cities, finish the game
        if not player_empire.alive() or not enemy_empire.alive():
            return

        interface.move_view(key, mouse_pos)
        # place objects on map
        if rendered is not None:
            game.objects.clear(world_map.Map().image, clear_callback)
        game.objects.update()
        rendered = game.objects.draw(world_map.Map().image)
        interface.draw_interface(screen)
        # show screen
        pygame.display.flip()
        # cap the framerate
        clock.tick(50)


play_game()
