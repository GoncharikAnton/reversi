from copy import deepcopy

class MiniMax:
    def __init__(self, model, depth):
        self.model = deepcopy(model)
        self.depth = depth
        # self.value = []


