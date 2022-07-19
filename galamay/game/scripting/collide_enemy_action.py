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

    #     for enemy in enemys:
    #         missile_body = missiles.get_body()
    #         enemy_body = enemy.get_body()

    #         if self._physics_service.has_collided(missile_body, enemy_body):
    #             sound = Sound(BOUNCE_SOUND)
    #             self._audio_service.play_sound(sound)
    #             points = enemy.get_points()
    #             stats.add_points(points)
    #             cast.remove_actor(ENEMY_GROUP, enemy)

        missiles_to_remove = set()
        enemys_to_remove = set()
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
                        missiles_to_remove.add(missile)
                        enemys_to_remove.add(enemy)
                        pass

            for enemy in enemys_to_remove:
                cast.remove_actor(ENEMY_GROUP, enemy)

            for missile in missiles_to_remove:
                cast.remove_actor(MISSILE_GROUP, missile)
        except TypeError:
            pass
