from event_bus import Events
from event_system.event import fire_event
from global_constants import SCREEN_HEIGHT
from finite_state_machine.state import State


class Move(State):

    ENEMY_SPEED = 2

    def on_update(self):
        enemy = self.fsm.owner
        enemy.y += self.ENEMY_SPEED
        if enemy.y > SCREEN_HEIGHT:
            fire_event(Events.ENEMY_OOB.name, enemy)
