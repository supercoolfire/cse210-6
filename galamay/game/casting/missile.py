import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Missile(Actor):
    """A solid, spherical object that is bounced around in the game."""

    def __init__(self, body, animation, debug=False):
        """Constructs a new Missile.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._is_launched = False

    def get_animation(self):
        """Gets the bat's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the missile's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the missle using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        if self._is_launched == False:
            """Steers the bat to the left."""
            velocity = Point(-MISSILE_VELOCITY, 0)
            self._body.set_velocity(velocity)

    def swing_right(self):
        if self._is_launched == False:
            """Steers the bat to the right."""
            velocity = Point(MISSILE_VELOCITY, 0)
            self._body.set_velocity(velocity)

    def stop_moving(self):
        if self._is_launched == False:
            """Stops the ship from moving."""
            velocity = Point(0, 0)
            self._body.set_velocity(velocity)

    def release(self):
        """Release the missile in a random direction."""
        self._is_launched = True
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-MISSILE_VELOCITY * rn, MISSILE_VELOCITY * rn])
        vy = -MISSILE_VELOCITY
        velocity = Point(0, vy)
        self._body.set_velocity(velocity)
