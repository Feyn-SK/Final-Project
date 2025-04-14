'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'
from state_class import state
import Dark_Blue_State

class Light_Blue(state):
    state = 1

    def action(self):
if 0 in self.neighbor:
    self.state=2
    else:
        False