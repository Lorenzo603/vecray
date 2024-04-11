import pyray as rl
from pyray import Vector2

from finite_state_machine.state_machine import FiniteStateMachine
from gameobjects.player.fsm.player_move_state import Move


class Player:

    def __init__(self, x, y, size, segments):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.segments = segments

        self.fsm = FiniteStateMachine(self, [Move()])
        self.fsm.start()

    def draw(self):
        self._draw_ship(self.x, self.y, self.size)
        # rl.draw_rectangle(
        # int(self.x - self.size / 2),
        # int(self.y - self.size / 2),
        # self.size, self.size, rl.RED)

    @staticmethod
    def _draw_ship(x, y, size):
        x = int(x)
        y = int(y)
        size = int(size)
        # Body
        rl.draw_line(x - size // 2, y - size // 2, x + size // 2, y - size // 2, rl.WHITE)  # Top
        rl.draw_line(x - size // 2, y + size // 2, x + size // 2, y + size // 2, rl.WHITE)  # Bottom
        rl.draw_line(x - size // 2, y - size // 2, x - size // 4, y - size, rl.WHITE)  # Top left
        rl.draw_line(x + size // 2, y - size // 2, x + size // 4, y - size, rl.WHITE)  # Top right
        rl.draw_line(x - size // 2, y + size // 2, x - size // 4, y + size, rl.WHITE)  # Bottom left
        rl.draw_line(x + size // 2, y + size // 2, x + size // 4, y + size, rl.WHITE)  # Bottom right
        rl.draw_line(x - size // 4, y - size, x - size // 4, y + size, rl.WHITE)  # Left side
        rl.draw_line(x + size // 4, y - size, x + size // 4, y + size, rl.WHITE)  # Right side

        # Cockpit
        rl.draw_line(x - size // 8, y - size // 2, x + size // 8, y - size // 2, rl.WHITE)  # Top
        rl.draw_line(x - size // 8, y - size // 2, x - size // 8, y - size // 4, rl.WHITE)  # Left
        rl.draw_line(x + size // 8, y - size // 2, x + size // 8, y - size // 4, rl.WHITE)  # Right
        rl.draw_line(x - size // 8, y - size // 4, x + size // 8, y - size // 4, rl.WHITE)  # Middle

        # Engines
        rl.draw_line(x - size // 2, y, x - size // 2 - size // 4, y, rl.WHITE)  # Left engine
        rl.draw_line(x + size // 2, y, x + size // 2 + size // 4, y, rl.WHITE)  # Right engine
