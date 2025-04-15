'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'
import numpy as np
import time
from Neighborhood import*
from State_Class import State

class Light_Blue(State):
    def __init__(self, row, col, parent_array, state = 1):
        super().__init__( row, col, parent_array, state = 1)  # Initialize parent class attributes


    def update_light_blue(self, dark_blue_counter):

        if (2 in self.neighborhood and dark_blue_counter < 5):
            return 1
        elif (2 in self.neighborhood and dark_blue_counter >= 5):
            return 2
        else:
            return 0


