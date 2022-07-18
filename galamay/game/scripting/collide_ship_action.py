from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideShipAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        missile = cast.get_first_actor(MISSILE_GROUP)
        ship = cast.get_first_actor(SHIP_GROUP)

        missile_body = missile.get_body()
        ship_body = ship.get_body()

        if self._physics_service.has_collided(missile_body, ship_body):
            missile.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
