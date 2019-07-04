from typing import Tuple
import pygame
# project modules #
from interface import empire_info, button, camera, minimap, selected_object_info, selected_object, selected_command
from game_objects import map
import configs
import singleton


def get_global_mouse_pos(mouse_pos: Tuple[int, int]) -> Tuple[int, int]:
    """ Mouse position with a glance to camera position on the map. """
    return mouse_pos[0] + Interface().camera.x, mouse_pos[1] + Interface().camera.y


class Interface(metaclass=singleton.Singleton):
    """ Interface is a facade which manages interface windows work. """

    def __init__(self, player_empire, enemy_empire):
        self.player_empire = player_empire
        self.camera = camera.Camera()
        self.selected_info = selected_object_info.Selected()
        self.minimap = minimap.Minimap()
        self.commands = pygame.sprite.Group()
        self.messages = pygame.sprite.Group()
        self.player_empire_info = empire_info.EmpireInfo(player_empire, enemy=False)
        self.enemy_empire_info = empire_info.EmpireInfo(enemy_empire, enemy=True)
        # The most recent chosen (selected) game object
        # and command respectively.
        self.selected_object = selected_object.SelectedObject()
        self.selected_command = selected_command.SelectedCommand()

    def move_view(self, key, mouse_pos: Tuple[int, int]):
        """ Moves camera and minimap frame. """
        self.camera.move_view(key, mouse_pos)
        self.minimap.move_frame(self.camera.topleft)

    def remove_all_info(self):
        """ Hides all selected object info (commands, features, etc. ). """
        self.commands.empty()
        self.selected_info.hide()
        self.selected_object.clear()
        self.selected_command.clear()

    def handle_interface_click(self, mouse_pos: Tuple[int, int]):
        """ Interface reaction to interface click (i.e. click any of interface windows handled). """

        for command in self.commands:
            if command.can_handle_click(mouse_pos):
                command.handle_click(mouse_pos)
                return True
        if self.selected_info.can_handle_click(mouse_pos):
            self.selected_info.handle_click(mouse_pos)
            return True
        if self.minimap.can_handle_click(mouse_pos):
            self.minimap.handle_click(mouse_pos)
            return True
        return False

    def handle_empty_click(self, mouse_pos: Tuple[int, int]):
        """ Interface reaction to empty click (i.e. click no object handled). """

        obj = self.selected_object.get()
        if obj is not None and obj.empire is self.player_empire:
            obj.handle_empty_click(get_global_mouse_pos(mouse_pos))
        command = self.selected_command.get()
        if command is not None:
            command.handle_empty_click(get_global_mouse_pos(mouse_pos))
        self.remove_all_info()

    def handle_object_click(self, obj):
        """ Interface reaction to object click (i.e. click any of objects handled). """

        selected_obj = self.selected_object.get()
        if selected_obj is not None and selected_obj.empire is self.player_empire:
            selected_obj.interact_with(obj)
        command = self.selected_command.get()
        if command is not None:
            command.handle_object_click(obj)
        self.selected_info.replace(obj)
        self.selected_object.replace(obj)
        self.selected_command.clear()
        self.commands.empty()
        # If given object belongs to player's empire,
        # let work with it. Otherwise do not show commands.
        if obj.empire is self.player_empire:
            self._place_commands(obj)

    def draw_interface(self, screen: pygame.Surface):
        """ Draws interface windows on `screen`. """

        # make place of camera location visible
        screen.blit(map.Map().image, (-self.camera.x, -self.camera.y))
        # draw interface windows
        self.selected_info.update()
        screen.blit(self.selected_info.image, self.selected_info.rect)
        self.minimap.update()
        screen.blit(self.minimap.image, self.minimap.rect)
        self.messages.update()
        self.messages.draw(screen)
        self.commands.draw(screen)
        self.player_empire_info.update()
        self.player_empire_info.draw(screen)
        self.enemy_empire_info.update()
        self.enemy_empire_info.draw(screen)

    def _place_commands(self, obj):
        """ Fill `self.commands`. """

        pos = [self.selected_info.rect.right + configs.SELECTED_TO_COMMAND_INDENT,
               configs.SCR_HEIGHT - configs.COMMAND_HEIGHT - 10]

        for command in obj.mouse_interaction_commands:
            command_window = button.MouseInteractionButton(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += configs.COMMANDS_INDENT

        for command in obj.no_interaction_commands:
            command_window = button.NoInteractionButton(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += configs.COMMANDS_INDENT

        for command in obj.object_interaction_commands:
            command_window = button.ObjectInteractionButton(*command)
            command_window.rect.topleft = pos
            self.commands.add(command_window)
            pos[0] += configs.COMMANDS_INDENT
