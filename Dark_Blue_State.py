from State_Class import State

class Dark_Blue(State):
    def __init__(self, row, col,parent_array, state = 4):
        super().__init__(row, col,parent_array, state = 4)  # Initialize parent class attributes

    def update_dark_blue(self):
        if 3 in self.neighborhood:
            return True
        else:
            return False
