from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveMissileAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        missile = cast.get_first_actor(MISSILE_GROUP)
        body = missile.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
