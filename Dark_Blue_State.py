'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'
from state_class import state
import time
import neighbor

class Dark_Blue(state):
    state = 2


#Notes about dark blue:

#After the light blue state becomes dark blue delay 1 second
time.sleep(1)

#After delay, check if there are any other dark blue states nearby



#if there are not any dark blue states nearby, move the dark blue state to a surrounding red state
def action(self, i, j):
    if self.state in self.neighbor:
    else:
        self.state = red


#This chain continues until another dark blue state is met in its neighborhood