import pygame


class Speed:
    def __init__(self, x_speed, y_speed):
        self.x = x_speed
        self.y = y_speed


class Car:
    def __init__(self):
        self.speed = None
        self.rect = None
        self.img = None


def play():
    def game_loop():
        speed = [2, 2]
        nonlocal car_rect
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pass
                    elif event.key == pygame.K_RIGHT:
                        pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pass
                    elif event.key == pygame.K_DOWN:
                        pass
                print(event)

            car_rect = car_rect.move(speed)
            if car_rect.left < 0 or car_rect.right > width:
                speed[0] = -speed[0]
            if car_rect.top < 0 or car_rect.bottom > height:
                speed[1] = -speed[1]
            screen.fill(black)
            screen.blit(car_rect, car)
            screen.display.flip()

    pygame.init()
    scr_size = width, height = 300, 300
    black = 0, 0, 0
    screen = pygame.display.set_mode(scr_size)
    pygame.display.set_caption("the Lord of the Rings")

    car = pygame.image.load("car.png")
    car_rect = car.get_rect()

    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    play()
