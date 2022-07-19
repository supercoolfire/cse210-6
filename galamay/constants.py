from game.casting.color import Color

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Shippy Chippy Bricks"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "assets/sounds/boing.wav"
WELCOME_SOUND = "assets/sounds/start.wav"
OVER_SOUND = "assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# MISSILE
MISSILE_GROUP = "missiles"
MISSILE_IMAGES = [f"assets/images/{n:03}.png" for n in range(0, 4)]
MISSILE_WIDTH = 20
MISSILE_HEIGHT = 28
MISSILE_VELOCITY = 6

# SHIP
SHIP_GROUP = "ships"
SHIP_IMAGES = [f"assets/images/{n:03}.png" for n in range(100, 103)]
SHIP_WIDTH = 70
SHIP_HEIGHT = 50
SHIP_RATE = 6
SHIP_VELOCITY = 7

# ENEMY
ENEMY_GROUP = "enemys"
ENEMY_IMAGES = {
    "b": [f"assets/images/{i:03}.png" for i in range(10, 19)],
    "g": [f"assets/images/{i:03}.png" for i in range(20, 29)],
    "p": [f"assets/images/{i:03}.png" for i in range(30, 39)],
    "y": [f"assets/images/{i:03}.png" for i in range(40, 49)]
}
ENEMY_WIDTH = 80
ENEMY_HEIGHT = 28
ENEMY_DELAY = 0.5
ENEMY_RATE = 4
ENEMY_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
HELP = "HELP"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
