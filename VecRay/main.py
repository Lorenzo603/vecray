import pyray as rl

from gameobjects.bullet.bullet_manager import BulletManager
from gameobjects.enemy.enemy import Enemy
from gameobjects.enemy.enemy_manager import EnemyManager
from gameobjects.player.player import Player
from global_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from stages.stage import draw_stage, w_shape_segments

PLAYER_SIZE = 50
NUM_ENEMIES = 10
ENEMY_SIZE = 30


def initialize_game_objects():
    _stage_segments = w_shape_segments(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 * 3, SCREEN_WIDTH // 8)
    _player = Player(_stage_segments[2][0].x, _stage_segments[2][0].y, PLAYER_SIZE, _stage_segments)
    _enemies = [
        Enemy(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, ENEMY_SIZE),
        Enemy(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 4 - 100, ENEMY_SIZE),
        Enemy(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 4 + 100, ENEMY_SIZE)
    ]

    return _stage_segments, _player, _enemies,


def draw():
    rl.clear_background(rl.BLACK)
    draw_stage(stage_segments)
    player.draw()
    for _bullet in bullet_manager.bullets:
        _bullet.draw()
    for _enemy in enemies:
        _enemy.draw()


# Initialize game
rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Tempest Clone")
rl.set_target_fps(60)

# create game objects
stage_segments, player, enemies = initialize_game_objects()
EnemyManager(enemies)
bullet_manager = BulletManager()


def update():
    player.fsm.update()

    if rl.is_key_pressed(rl.KeyboardKey.KEY_SPACE):
        bullet_manager.spawn_bullet(player.x, player.y - player.size / 2)

    for bullet in bullet_manager.bullets:
        bullet.fsm.update()

    for enemy in enemies:
        enemy.fsm.update()


while not rl.window_should_close():
    update()
    rl.begin_drawing()
    draw()
    rl.end_drawing()
# Clean up
rl.close_window()
