'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'
from Neighborhood import neighbor as nbh
from State_Class import State

class Red(State):
    def __init__(self, row, col, parent_array, state = 3):
        super().__init__( row, col, parent_array, state = 3)  # Initialize parent class attributes

def action(self,i,j):
    if 2 in self.neighborhood:
        return True
    else:
        return False
#refrence function when red turns into dark blue







