import pyray as rl

from finite_state_machine.state_machine import FiniteStateMachine
from gameobjects.bullet.fsm.bullet_move_state import Move


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.fsm = FiniteStateMachine(self, [Move()])
        self.fsm.start()

    def draw(self):
        rl.draw_rectangle(int(self.x), int(self.y), 5, 10, rl.WHITE)
