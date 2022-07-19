from constants import *
from game.scripting.action import Action


class ControlMissileAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        missile = cast.get_first_actor(MISSILE_GROUP)
        if self._keyboard_service.is_key_down(LEFT):
            missile.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT):
            missile.swing_right()
        else:
            missile.stop_moving()
