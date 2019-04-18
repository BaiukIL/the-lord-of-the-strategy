import pygame
from realization import gameconfig, player as player_mod
from abstraction import empire, races


def list_of_clicked(group: pygame.sprite.Group, mouse_pos: tuple) -> list:
    clicked = []
    for obj in group:
        if obj.rect.collidepoint(mouse_pos):
            clicked.append(obj)
    return clicked


def play_game():
    world_map = pygame.Surface((6000, 3000))
    world_map.fill((0, 150, 0))

    player = player_mod.Player(world_map=world_map)

    selected = pygame.Surface((100, 100))
    selected.set_alpha(0)

    this_empire = empire.Empire(races.elves)
    this_empire.set_city("Nre")
    barrack = this_empire.get_city("Nre").build_barrack()

    # interface = pygame.sprite.Group()
    objects = pygame.sprite.Group()

    # interface.add(selected)
    objects.add(barrack)

    while True:
        mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = True
            print(event)
        key = pygame.key.get_pressed()
        mouse_pos = (pygame.mouse.get_pos()[0] + player.camera.x, pygame.mouse.get_pos()[1] + player.camera.y)

        if mouse_pressed:
            clicked = list_of_clicked(objects, mouse_pos)
            if len(clicked) != 0:
                for obj in clicked:
                    selected = obj.click_react()
            else:
                selected.set_alpha(0)

        player.move(key, mouse_pos)

        world_map.fill((0, 150, 0))
        objects.draw(world_map)

        screen.blit(world_map, (-player.camera.x, -player.camera.y))
        screen.blit(selected, (0, 0))
        pygame.display.flip()

        # cap the framerate
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(gameconfig.SCR_SIZE)
    pygame.display.set_caption("the Lord of the Strategy")
    icon_surf = pygame.image.load(gameconfig.ICON)
    pygame.display.set_icon(icon_surf)
    clock = pygame.time.Clock()

    play_game()
