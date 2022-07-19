from constants import *
from game.scripting.action import Action


class DrawMissileAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        missiles = cast.get_actors(MISSILE_GROUP)
        for missile in missiles:
            body = missile.get_body()

            if missile.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)

            # animate missile
            animation = missile.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
