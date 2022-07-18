from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.missile import Missile


class ControlShipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        missile = cast.get_first_actor(MISSILE_GROUP)
        if self._keyboard_service.is_key_down(LEFT):
            ship.swing_left()
            missile.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT):
            ship.swing_right()
            missile.swing_right()
        else:
            ship.stop_moving()

        if self._keyboard_service.is_key_down(SPACE):
            # fire
            missile = cast.get_first_actor(MISSILE_GROUP)
            missile.release()
            # create another missle ready
