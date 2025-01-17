from constants import *
from game.casting.point import Point
from game.scripting.action import Action
from game.services.raylib.raylib_mouse_service import RaylibMouseService


class MoveShipAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        body = ship.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()

        position = position.add(velocity)
        # position = position.add(RaylibMouseService.get_coordinates(self))

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - SHIP_WIDTH):
            position = Point(SCREEN_WIDTH - SHIP_WIDTH, position.get_y())

        body.set_position(position)
