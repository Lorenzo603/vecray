import pyray as rl


def draw_w_shape(x, y, size):
    x = int(x)
    y = int(y)
    size = int(size)

    rl.draw_line(x - size, y + size, x - size // 2, y - size, rl.WHITE)
    rl.draw_line(x - size // 2, y - size, x, y + size, rl.WHITE)
    rl.draw_line(x, y + size, x + size // 2, y - size, rl.WHITE)
    rl.draw_line(x + size // 2, y - size, x + size, y + size, rl.WHITE)
