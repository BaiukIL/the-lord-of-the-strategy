import pygame
from typing import Text
# project modules #
from windows import window
import configs


class Selected(window.Window):
    """ A window which is located in the left bottom corner of the screen
    and responsible for showing selected object information. """

    def __init__(self):
        window.Window.__init__(self, configs.SELECTED_SIZE)
        self.rect.bottomleft = (0, configs.SCR_HEIGHT)
        self.text = str()
        self.set_default_alpha(170)
        self.set_never_bordered()
        self.hide()

    def action_while_hide(self):
        self.clear()

    def replace(self, obj):
        self.clear()
        self.active()
        self._place_object_image(obj.image)
        self._place_object_text(obj.info())
        self._show_empire_info(obj.empire)

    def _show_empire_info(self, empire):
        pass

    def _place_object_image(self, image: pygame.Surface):
        selected_img_side_size = min(self.rect.width // 2, self.rect.height // 2)
        self.image.blit(pygame.transform.scale(image, (selected_img_side_size,
                                                            selected_img_side_size)),
                             (self.rect.width // 2, self.rect.height // 2))

    def _place_object_text(self, text: Text):
        font = pygame.font.SysFont(name='Ani', size=20)
        # vertical indent between lines
        indent = 25
        # interface_config.BORDERS_SIZE is indent from left side of selected screen
        line_pos = [0, 0]
        for line in text.split('\n'):
            self.image.blit(font.render(line, True, (0, 0, 0)), line_pos)
            line_pos[1] += indent
