import pyray as rl

from finite_state_machine.state_machine import FiniteStateMachine
from gameobjects.enemy.fsm.enemy_move_state import Move


class Enemy:

    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size

        self.fsm = FiniteStateMachine(self, [Move()])
        self.fsm.start()

    def draw(self):
        rl.draw_rectangle(int(self.x - self.size/2), int(self.y - self.size/2), self.size, self.size, rl.GREEN)
