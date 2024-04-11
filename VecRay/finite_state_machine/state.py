from finite_state_machine.state_machine import FiniteStateMachine


class State:

    def __init__(self):
        self.fsm = None

    def on_enter(self, fsm: FiniteStateMachine):
        self.fsm = fsm
        pass

    def on_exit(self):
        pass

    def on_update(self):
        pass

    def on_draw(self):
        pass
