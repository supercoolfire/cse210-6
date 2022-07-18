from constants import *
from game.casting.ship import Ship
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.missile import Missile


class CollideEnemyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        missile = cast.get_first_actor(MISSILE_GROUP)
        enemys = cast.get_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for enemy in enemys:
            missile_body = missile.get_body()
            enemy_body = enemy.get_body()

            if self._physics_service.has_collided(missile_body, enemy_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = enemy.get_points()
                stats.add_points(points)
                cast.remove_actor(ENEMY_GROUP, enemy)

                # create new missile
                # cast.remove_actor(MISSILE_GROUP, missile)
                # position = Point(x, y)
                # size = Point(MISSILE_WIDTH, MISSILE_HEIGHT)
                # velocity = Point(0, 0)
                # body = Body(position, size, velocity)
                # image = Image(MISSILE_IMAGE)
                # missile = Missile(body, image, True)
                # cast.add_actor(MISSILE_GROUP, missile)
