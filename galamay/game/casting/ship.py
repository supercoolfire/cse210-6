from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.missile import Missile
from game.casting.body import Body
from game.casting.image import Image
from game.casting.animation import Animation


class Ship(Actor):
    """A implement used to hit and bounce the missile in the game."""

    def __init__(self, body, animation, debug=False):
        """Constructs a new Bat.

        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the bat's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the bat's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(SHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def launch(self, cast):
        position = self._body.get_position()
        size = Point(MISSILE_WIDTH, MISSILE_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(MISSILE_IMAGES, MISSILE_HEIGHT)
        missile = Missile(body, animation, True)
        missile.release()
        cast.add_actor(MISSILE_GROUP, missile)

    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
