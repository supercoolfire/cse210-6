from ctypes.wintypes import POINT
from game.casting.actor import Actor


class Enemy(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, debug=False):
        """Constructs a new Enemy.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        self._set_velocity = POINT(0, 5)

    def get_animation(self):
        """Gets the enemy's image.

        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the enemy's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the enemy's points.

        Returns:
            A number representing the enemy's points.
        """
        return self._points

    def enemy_velocity(self):

        return self._set_velocity
