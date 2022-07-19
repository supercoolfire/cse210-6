from constants import *
from game.scripting.action import Action


class MoveMissileAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        missiles = cast.get_actors(MISSILE_GROUP)
        for missile in missiles:
            body = missile.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
