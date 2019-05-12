import os
import sys
import pygame
from game import Game
from AI import AI
from interface.interface import Interface, get_global_mouse_pos
import configs
from game_objects import empire, races
from images import image as img
import map


def clear_callback(surf, rect):
    surf.fill(map.Map().color, rect)


def finish_game(win: bool):
    if win:
        pygame.draw.rect(screen, pygame.Color('yellow'), screen.get_rect())
        final_message = 'You win!'
    else:
        pygame.draw.rect(screen, pygame.Color('red'), screen.get_rect())
        final_message = 'You lost...'
    font = pygame.font.SysFont(name='Ani', size=100)
    screen.blit(font.render(final_message, True, pygame.Color('black')),
                (screen.get_width() // 3 + 80, screen.get_height() // 5))
    screen.blit(font.render('To restart the game, press S.', True, pygame.Color('black')),
                (screen.get_width() // 6, screen.get_height() // 4 + 150))
    screen.blit(font.render('To exit, press ESC.', True, pygame.Color('black')),
                (screen.get_width() // 4 + 30, screen.get_height() // 4 + 300))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                os.execl(sys.executable, sys.executable, *sys.argv)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return


def play_game():
    my_empire = empire.Empire(races.ORCS, name='MyEmpire')
    enemy_empire = empire.Empire(races.DWARFS, name='Erewen')
    AI(enemy_empire)
    Interface(my_empire, enemy_empire)

    my_empire.set_city("Nevborn")
    my_city = my_empire.get_city("Nevborn")
    my_city.rect.x = 500
    my_city.rect.centery = map.Map().rect.centery

    enemy_empire.set_city("Nuhen")
    enemy_city = enemy_empire.get_city("Nuhen")
    enemy_city.rect.right = map.Map().rect.right - 4000
    enemy_city.rect.centery = map.Map().rect.centery

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
            print(event)

        key = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pressed:
            handled = False
            # check if any of interface windows can handle click
            if Interface().handle_click(mouse_pos):
                handled = True
            else:
                for obj in Game().objects:
                    # check if any of game objects can handle click
                    if obj.handle_click(get_global_mouse_pos(mouse_pos)):
                        handled = True
            if not handled:
                Interface().handle_empty_click(mouse_pos)

        AI().play_step()

        # If any of empires is out of cities, finish the game
        if not my_empire.alive() or not enemy_empire.alive():
            finish_game(win=my_empire.alive())
            break

        Interface().move_view(key, mouse_pos)
        # place objects on map
        if rendered is not None:
            Game().objects.clear(map.Map().image, clear_callback)
        Game().objects.update()
        rendered = Game().objects.draw(map.Map().image)
        Interface().draw_interface(screen)
        # show screen
        pygame.display.flip()
        # cap the framerate
        clock.tick(50)


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(configs.SCR_SIZE)
    pygame.display.set_caption("the Lord of the Strategy")
    icon_surf = img.get_image().ICON
    pygame.display.set_icon(icon_surf)
    clock = pygame.time.Clock()

    if not pygame.font.get_init():
        raise SystemExit("Fonts are out-of-service")

    play_game()
