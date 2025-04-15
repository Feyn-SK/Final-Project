'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'
from Neighborhood import neighbor as nbh
from State_Class import State

class Black(State):
    def __init__(self, row, col, parent_array, state = 2):
        super().__init__(row, col, parent_array, state = 2)  # Initialize parent class attributes





