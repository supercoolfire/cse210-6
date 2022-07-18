from constants import *
from game.scripting.action import Action


class DrawEnemysAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        enemys = cast.get_actors(ENEMY_GROUP)

        for enemy in enemys:
            body = enemy.get_body()

            if enemy.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)

            animation = enemy.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
