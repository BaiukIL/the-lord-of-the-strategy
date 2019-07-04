import pygame
# project modules #
from windows import window
from game_objects import map
import configs


class Minimap(window.Window):
    """ A window which is a brief version of the map.
    Located in the right bottom of the screen. """

    def __init__(self):
        window.Window.__init__(
            self, configs.MINIMAP_SIZE,
            image=pygame.transform.scale(map.Map().image, configs.MINIMAP_SIZE))
        self.rect.bottomright = configs.SCR_SIZE
        self.set_constant_bordered()
        self.set_default_alpha(255)

        # `frame` on the minimap is a camera on the map.
        self._frame = pygame.Rect(self.rect.topleft, (
            self.rect.width * configs.SCR_WIDTH // map.Map().rect.width,
            self.rect.height * configs.SCR_HEIGHT // map.Map().rect.height))

    def move_frame(self, pos: tuple):
        """ Moves frame at `pos` position.
        `pos` must be real map position i.e. position with a glance to current camera offset. """
        self._frame.x = pos[0] * self.rect.width // map.Map().rect.width
        self._frame.y = pos[1] * self.rect.height // map.Map().rect.height

    def action_while_update(self):
        self.clear()
        self.image.blit(pygame.transform.scale(
            map.Map().image, self.rect.size), (0, 0))
        pygame.draw.rect(self.image, self._borders_color, self._frame, 1)
