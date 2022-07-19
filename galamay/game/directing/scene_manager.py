import csv
from constants import *
from game.casting.animation import Animation
from game.casting.missile import Missile
from game.casting.body import Body
from game.casting.enemy import Enemy
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.ship import Ship
from game.casting.stats import Stats
from game.casting.text import Text
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_enemy_action import CollideEnemyAction
from game.scripting.collide_ship_action import CollideShipAction
from game.scripting.control_ship_action import ControlShipAction
from game.scripting.draw_missile_action import DrawMissileAction
from game.scripting.draw_enemys_action import DrawEnemysAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_ship_action import DrawShipAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_missile_action import MoveMissileAction
from game.scripting.move_ship_action import MoveShipAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(
        PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_ENEMYS_ACTION = CollideEnemyAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_SHIP_ACTION = CollideShipAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_SHIP_ACTION = ControlShipAction(KEYBOARD_SERVICE)
    DRAW_MISSILE_ACTION = DrawMissileAction(VIDEO_SERVICE)
    DRAW_ENEMYS_ACTION = DrawEnemysAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_SHIP_ACTION = DrawShipAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(
        AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_MISSILE_ACTION = MoveMissileAction()
    MOVE_SHIP_ACTION = MoveShipAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        # self._add_missile(cast) # do not show missile on startup
        self._add_enemys(cast)
        self._add_ship(cast)
        self._add_dialog(cast, ENTER_TO_START)
        self._add_dialog2(cast, HELP)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        cast.clear_actors(MISSILE_GROUP)  # decommision ordnance every level
        # self._add_missile(cast) # do not show missile on level start
        self._add_enemys(cast)
        self._add_ship(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(
            self.AUDIO_SERVICE, WELCOME_SOUND))

    def _prepare_try_again(self, cast, script):
        self._add_missile(cast)
        self._add_ship(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        # self._activate_missile(cast) # stop launcing missile on startup
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_SHIP_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_missile(cast)
        self._add_ship(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _activate_missile(self, cast):
        missile = cast.get_first_actor(MISSILE_GROUP)
        missile.release()

    def _add_missile(self, cast):
        cast.clear_actors(MISSILE_GROUP)
        x = CENTER_X - MISSILE_WIDTH / 2
        y = SCREEN_HEIGHT - SHIP_HEIGHT - MISSILE_HEIGHT
        position = Point(x, y)
        size = Point(MISSILE_WIDTH, MISSILE_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        # image = Image(MISSILE_IMAGES)
        animation = Animation(MISSILE_IMAGES, MISSILE_RATE)
        missile = Missile(body, animation, True)
        cast.add_actor(MISSILE_GROUP, missile)

    def _add_enemys(self, cast):
        cast.clear_actors(ENEMY_GROUP)

        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * ENEMY_WIDTH
                    y = FIELD_TOP + r * ENEMY_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = ENEMY_POINTS

                    if frames == 1:
                        points *= 2

                    position = Point(x, y)
                    size = Point(ENEMY_WIDTH, ENEMY_HEIGHT)
                    velocity = Point(0, 5)
                    images = ENEMY_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, ENEMY_RATE, ENEMY_DELAY)

                    enemy = Enemy(body, animation, points)
                    cast.add_actor(ENEMY_GROUP, enemy)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)
        pass

    # FOR HELP
    def _add_dialog2(self, cast, message):
        # cast.clear_actors(DIALOG_GROUP) # prevent PRESS ENTER TO START from hiding
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y + 100)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_ship(self, cast):
        cast.clear_actors(SHIP_GROUP)
        x = CENTER_X - SHIP_WIDTH / 2
        y = SCREEN_HEIGHT - SHIP_HEIGHT
        position = Point(x, y)
        size = Point(SHIP_WIDTH, SHIP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(SHIP_IMAGES, SHIP_RATE)
        ship = Ship(body, animation)
        cast.add_actor(SHIP_GROUP, ship)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_MISSILE_ACTION)
        script.add_action(OUTPUT, self.DRAW_ENEMYS_ACTION)
        script.add_action(OUTPUT, self.DRAW_SHIP_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_MISSILE_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ENEMYS_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
