# The first stte in the list is the initial one
class FiniteStateMachine:
    def __init__(self, owner, states):
        self.current_state = None
        self.owner = owner
        self.states = states

    def start(self):
        self.change_state(self.states[0])

    def update(self):
        if self.current_state:
            self.current_state.on_update()

    def change_state(self, new_state):
        if self.current_state:
            self.current_state.on_exit()
        self.current_state = new_state
        self.current_state.on_enter(self)

