import pygame
from pygame_realization import interface as itf, map
from configs import interface_config
from entities import empire, races
from images import image


def play_game():
    interface = itf.Interface()

    this_empire = empire.Empire(races.elves)
    this_empire.set_city("Nevborn")

    objects = pygame.sprite.Group()
    objects.add(this_empire.get_city("Nevborn"))

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
            if itf.Selected().rect.collidepoint(mouse_pos):
                handled = True
            if itf.Minimap().rect.collidepoint(mouse_pos):
                handled = True
            for command in interface.commands:
                if command.rect.collidepoint(mouse_pos):
                    handled = True
            for obj in objects:
                # mouse position with a glance to camera position on the map
                mouse_global_pos = mouse_pos[0] + itf.Camera().x, mouse_pos[1] + itf.Camera().y
                if obj.rect.collidepoint(mouse_global_pos):
                    interface.handle_object_click(obj.handle())
                    handled = True
            if not handled:
                interface.handle_no_click()

        # place objects on map
        objects.draw(map.Map().image)
        interface.move_view(key, mouse_pos)
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
