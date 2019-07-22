""" This module starts the game.
To start one, put `python3 play_game.py` in terminal. """


import os
import sys
import pygame
# project modules #
import user_configs
import game_configs as configs
from game import Game
from game_objects import races
from game_objects.empire import Empire
from world_map import Map
from ai import AI
from interface.interface_class import Interface
from interface import click_handler
from display import Display
import image as img


def place_objects_on_display():
    """ Finds what objects can be displayed onto the screen and displays them. """
    for obj in pygame.sprite.spritecollide(Display(), Game().objects, False):
        Display().image.blit(obj.image, (obj.rect.x -
                                         Interface().camera.x, obj.rect.y - Interface().camera.y))


def _wait_for_command():
    """ Is called when game has finished. """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.KEYDOWN:
                os.execl(sys.executable, sys.executable, *sys.argv)


def finish_game(win: bool, screen: pygame.Surface):
    """ Is called when game is finished. """

    if win:
        pygame.draw.rect(screen, pygame.Color('yellow'), screen.get_rect())
        final_message = 'You win!'
    else:
        pygame.draw.rect(screen, pygame.Color('red'), screen.get_rect())
        final_message = 'You lost...'
    # Set font.
    font = pygame.font.SysFont(name='Ani', size=100)
    # Place messages.
    screen.blit(font.render(final_message, True, pygame.Color('black')),
                (screen.get_width() // 3 + 80, screen.get_height() // 5))
    screen.blit(font.render('To exit, press ESC.', True, pygame.Color('black')),
                (screen.get_width() // 6, screen.get_height() // 4 + 150))
    screen.blit(font.render('To restart the game, press any other button.', True, pygame.Color('black')),
                (screen.get_width() // 4 + 30, screen.get_height() // 4 + 300))
    # Display changes.
    pygame.display.update()

    _wait_for_command()


def play_game():
    """ Starts the game. """

    # Game objects initialization starts.
    player_empire = Empire(user_configs.EMPIRE_RACE,
                           name=user_configs.EMPIRE_NAME)
    enemy_empire = Empire(races.DWARFS, name='Durden')

    # Initialize game singletons.
    Game(player_empire, enemy_empire)
    Interface(player_empire, enemy_empire)
    Display(SCREEN)

    player_empire.set_city(user_configs.CITY_NAME)
    player_default_city = player_empire.get_city(user_configs.CITY_NAME)
    player_default_city.rect.x = 500
    player_default_city.rect.centery = Map().rect.centery

    enemy_empire.set_city("Nuhen")
    enemy_default_city = enemy_empire.get_city("Nuhen")
    enemy_default_city.rect.right = Map().rect.right - 700
    enemy_default_city.rect.centery = Map().rect.centery

    AI(enemy_empire)
    # Game objects initialization ends.

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
            click_handler.handle_click(mouse_pos)

        # AI is singleton, which has been initialized before.
        AI().play_step()

        # If any of empires is out of cities, the game is finished.
        if not player_empire.alive() or not enemy_empire.alive():
            finish_game(win=player_empire.alive(), screen=SCREEN)
            return

        Interface().move_view(key, mouse_pos)
        # Update objects.
        # It looks weird, but use Game().objects.update() causes an error in
        # specific case: if one of objects is killed during `update`, its `update`
        # method is still called. It happens because Game().objects.update() updates
        # ALL sprites which are contained in Game().objects at the moment of
        # Game().objects.update() is called.
        for obj in Game().objects:
            if obj in Game().objects:
                obj.update()
        # Make place of camera location visible.
        SCREEN.blit(Map().image, (-Interface().camera.x, -Interface().camera.y))

        place_objects_on_display()

        Interface().draw_interface(SCREEN)

        # Show screen.
        pygame.display.update()
        # Cap the framerate.
        CLOCK.tick(50)


if __name__ == '__main__':
    # pygame initialization.
    pygame.init()
    tmp = pygame.display.set_mode(configs.SCR_SIZE)
    pygame.display.set_caption("the Lord of the Strategy")
    pygame.display.set_icon(img.get_image().ICON)
    if not pygame.font.get_init():
        raise SystemExit("Fonts are out-of-service")
    # Global variables initilization.
    SCREEN = tmp
    CLOCK = pygame.time.Clock()

    play_game()
