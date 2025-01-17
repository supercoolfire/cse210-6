from constants import *
from game.scripting.action import Action


class ControlShipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        if self._keyboard_service.is_key_down(LEFT):
            ship.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT):
            ship.swing_right()
        else:
            ship.stop_moving()

        # 1 launch per key press
        if self._keyboard_service.is_key_pressed(SPACE):
            ship.launch(cast)
