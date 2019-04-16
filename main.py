import pygame
from realization import gameconfig, player as player_mod
from abstraction.buildings import barrack


def play_game():
    # my_empire = empire.Empire(race=races.elves)
    # my_empire.set_city("Guin")

    # world_map = pygame.image.load(gameconfig.MAP)
    world_map = pygame.Surface((6000, 3000))
    world_map.fill((0, 150, 0))

    player = player_mod.Player(world_map=world_map)

    barrack_obj = barrack.ElvesBarrack(10, None)
    barrack_obj.image = pygame.image.load('images/barrack.png')

    objects = pygame.sprite.Group()
    objects.add(barrack_obj)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            print(event)

        key = pygame.key.get_pressed()
        mouse_pos = (pygame.mouse.get_pos()[0] + player.camera.x, pygame.mouse.get_pos()[1] + player.camera.y)

        # for obj in objects:

        player.move(key, mouse_pos)

        world_map.fill((0, 150, 0))
        # world_map.blit(barrack, barrack_rect)
        screen.blit(world_map, (-player.camera.x, -player.camera.y))
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

    city.City.image = pygame.image.load(gameconfig.ICON)

    play_game()
