from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.missile import Missile


class ControlMissileAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        pass
        # missile = cast.get_first_actor(MISSILE_GROUP)
        # if self._keyboard_service.is_key_down(LEFT):
        #     missile.swing_left()
        # elif self._keyboard_service.is_key_down(RIGHT):
        #     missile.swing_right()
        # else:
        #     missile.stop_moving()
