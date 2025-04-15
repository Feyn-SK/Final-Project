'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'
from state_class import state

class Black(state):
    state = 4

    def action(self):
        neighbor_states = list(self.neighbhorhood[0])
        neighbor_locs = list(self.neighbhorhood[1])
        
        if 1 in neighbor_states:
            light_blue_index = neighbor_states.index(1)
            
            count_black = 0
            for i, s in enumerate(neighbor_states):
                if s == 4 and i != light_blue_index:
                    count_black += 1

            if count_black == 0:
                return True, light_blue_index 
        return False, None
