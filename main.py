import pygame
from game import Game
from interface.interface import Interface, get_global_mouse_pos
from configs import interface_config
from game_objects import empire, races, map
from images import image


def play_game():
    this_empire = empire.Empire(races.ELVES)
    this_empire.set_city("Nevborn")

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
            handled = Interface().handle_click(mouse_pos)
            for obj in Game().objects:
                if obj.handle_click(get_global_mouse_pos()):
                    handled = True
            if not handled:
                Interface().handle_empty_click()

        Interface().move_view(key, mouse_pos)

        map.Map().clear()
        # place objects on map
        Game().objects.draw(map.Map().image)
        Interface().draw_interface(screen)
        # show screen
        pygame.display.flip()
        # cap the framerate
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(interface_config.SCR_SIZE)
    pygame.display.set_caption("the Lord of the Strategy")
    icon_surf = pygame.image.load(image.ICON)
    pygame.display.set_icon(icon_surf)
    clock = pygame.time.Clock()

    if not pygame.font.get_init():
        raise SystemExit("Fonts are out-of-service")

    play_game()
