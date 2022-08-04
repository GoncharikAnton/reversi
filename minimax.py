from copy import deepcopy

class MiniMax:

    def __init__(self, model, depth):
        self.model = deepcopy(model)
        self.depth = depth
        self.value = []

# state : board, 1_possible_step
    def value(self, state):
        if state is terminal_state:
            return state.utility
        if self.model.player.X:
            return self.max_value(state)
        if self.model.player.O:
            return self.min_value(state)

    def max_value(self, state):
        v = int('-inf')
        for successor in state:
            v = max(v, value(successor))
        return v

    def min_value(self, state):
        v = int('inf')
        for successor in state:
            v = min(v, value(successor))
        return v
