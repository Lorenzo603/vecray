import pyray as rl
from finite_state_machine.state import State


class Move(State):

    PLAYER_SPEED = 5

    def on_update(self):
        player = self.fsm.owner
        if rl.is_key_down(rl.KeyboardKey.KEY_LEFT):
            player.x -= self.PLAYER_SPEED
        if rl.is_key_down(rl.KeyboardKey.KEY_RIGHT):
            player.x += self.PLAYER_SPEED
        if rl.is_key_down(rl.KeyboardKey.KEY_UP):
            player.y -= self.PLAYER_SPEED
        if rl.is_key_down(rl.KeyboardKey.KEY_DOWN):
            player.y += self.PLAYER_SPEED
