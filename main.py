import pygame
from pygame_realization import interface as interface_mod, base_handler
from configs import game_config, interface_config
from entities import empire, races
from images import image


def play_game():
    world_map = pygame.transform.scale(pygame.image.load(game_config.BACKGROUND), (5500, 5500))

    interface = interface_mod.Interface(world_map)

    this_empire = empire.Empire(races.elves)
    this_empire.set_city("Nevborn")

    objects = pygame.sprite.Group()
    objects.add(this_empire.get_city("Nevborn"))

    while True:
        mouse_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
            print(event)

        key = pygame.key.get_pressed()
        # consider camera position while getting the mouse position
        mouse_pos = (pygame.mouse.get_pos()[0] + interface.camera.x, pygame.mouse.get_pos()[1] + interface.camera.y)

        if mouse_pressed:
            handled = False
            for obj in objects:
                if obj.rect.collidepoint(mouse_pos):
                    interface.handle_object_click(obj.react_click())
                    handled = True
            if not handled:
                interface.handle_no_click()

        interface.camera.move_view(key, mouse_pos)
        # place objects on map
        objects.draw(world_map)
        # draw interface windows
        interface.draw_windows(screen)
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
