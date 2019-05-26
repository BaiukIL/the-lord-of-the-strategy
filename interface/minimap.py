import pygame
# project modules #
from windows import window
from game_objects import map
import configs


class Minimap(window.Window):
    """A window which is located in the right bottom of the screen.
    Shows camera place at the map."""

    def __init__(self):
        window.Window.__init__(self, configs.MINIMAP_SIZE, image=map.Map().image)
        self.rect.bottomright = configs.SCR_SIZE
        self.set_constant_bordered()
        self.set_default_alpha(170)

        self._frame = pygame.Rect(
            self.rect.topleft, (
                int(self.rect.width * configs.SCR_WIDTH / map.Map().rect.width),
                int(self.rect.height * configs.SCR_HEIGHT / map.Map().rect.height)))

    def move_frame(self, pos: tuple):
        self._frame.x = int(pos[0] * self.rect.width / map.Map().rect.width)
        self._frame.y = int(pos[1] * self.rect.height / map.Map().rect.height)

    def action_while_update(self):
        self.clear()
        self.real_image.blit(pygame.transform.scale(map.Map().image, self.rect.size), (0, 0))
        pygame.draw.rect(self.real_image, self._borders_color, self._frame, 1)
