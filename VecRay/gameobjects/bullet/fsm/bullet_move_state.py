from event_bus import Events
from event_system.event import fire_event
from finite_state_machine.state import State


class Move(State):

    BULLET_SPEED = 10

    def on_update(self):
        bullet = self.fsm.owner
        bullet.y -= self.BULLET_SPEED
        if bullet.y < 0:
            fire_event(Events.BULLET_OOB.name, bullet)
