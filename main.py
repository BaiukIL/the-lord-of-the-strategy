import pygame
from interface import interface as itf
from configs import interface_config
from game_objects import empire, races, map
from images import image


def get_global_mouse_pos() -> tuple:
    """Mouse position with a glance to camera position on the map"""

    mouse_pos = pygame.mouse.get_pos()
    return mouse_pos[0] + itf.Interface().camera.x, mouse_pos[1] + itf.Interface().camera.y


def play_game():
    interface = itf.Interface()

    this_empire = empire.Empire(races.ELVES)
    this_empire.set_city("Nevborn")

    objects = pygame.sprite.Group()
    city = this_empire.get_city("Nevborn")
    objects.add(city)

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
            handled = itf.Interface().handle_click(mouse_pos)
            for obj in objects:
                if obj.handle_click(get_global_mouse_pos()):
                    handled = True
            if not handled:
                interface.handle_no_click()

        # place objects on map
        objects.draw(map.Map().image)
        interface.move_view(key, mouse_pos)

        interface.draw_interface(screen)
        if itf.Interface().selected.buffer is not None:
            screen.blit(itf.Interface().selected.buffer._reset_image, (400, 100))
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
