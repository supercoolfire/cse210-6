from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideEnemyAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        missiles = cast.get_actors(MISSILE_GROUP)
        enemys = cast.get_actors(ENEMY_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        try:
            for missile in missiles:
                for enemy in enemys:
                    missile_body = missile.get_body()
                    enemy_body = enemy.get_body()

                    if self._physics_service.has_collided(missile_body, enemy_body):
                        sound = Sound(BOUNCE_SOUND)
                        self._audio_service.play_sound(sound)
                        points = enemy.get_points()
                        stats.add_points(points)
                        cast.remove_actor(MISSILE_GROUP, missile)
                        cast.remove_actor(ENEMY_GROUP, enemy)
        except TypeError:
            pass
