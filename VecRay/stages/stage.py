import pyray as rl
from pyray import Vector2


def draw_stage(segments):
    for segment in segments:
        rl.draw_line(int(segment[0].x), int(segment[0].y), int(segment[1].x), int(segment[1].y), rl.WHITE)


def w_shape_segments(x, y, size):
    segments = [
        (Vector2(x - size, y + size), Vector2(x - size // 2, y - size)),
        (Vector2(x - size // 2, y - size), Vector2(x, y + size)),
        (Vector2(x, y + size), Vector2(x + size // 2, y - size)),
        (Vector2(x + size // 2, y - size), Vector2(x + size, y + size))
    ]
    return segments
