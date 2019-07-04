from typing import Tuple
# project modules #
import singleton
from game import Game
from interface.interface import Interface


def get_global_mouse_pos(mouse_pos: Tuple[int, int]) -> Tuple[int, int]:
    """Mouse position with a glance to camera position on the map"""
    return mouse_pos[0] + Interface().camera.x, mouse_pos[1] + Interface().camera.y


def handle_click(mouse_pos: Tuple[int, int]):
    handled = False
    # tell interface to handle click
    if Interface().handle_interface_click(mouse_pos):
        handled = True
    #     if interface couldn't handle click, tell objects to handle one
    else:
        for obj in Game().objects:
            if obj.handle_click(get_global_mouse_pos(mouse_pos)):
                handled = True
    if not handled:
        Interface().handle_empty_click(mouse_pos)


# it's a class because it will have field connected with empires
class ClickHandler(metaclass=singleton.Singleton):
    @staticmethod
    def handle_object_first_click(obj):
        Interface().handle_object_click(obj)

    @staticmethod
    def handle_object_second_click(obj):
        Interface().remove_all_info()

    @staticmethod
    def handle_object_kill(obj):
        if Interface().selected_object.get() is obj:
            Interface().remove_all_info()

    @staticmethod
    def handle_command_first_click(command):
        Interface().selected_command.replace(command)

    @staticmethod
    def handle_command_second_click(command):
        Interface().selected_command.clear()

    @staticmethod
    def handle_command_bad_execution(error_message):
        Interface().messages.add(error_message)
