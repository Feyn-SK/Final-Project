'States: 0:white, 1:light_blue, 2: Dark_blue, 3: red, 4:black'

state=4

def action(self, i, j):
    if self.state in self.neighbor:
        return True

    elif 1 in self.neighborhood:
        index_of = self.neighbhorhood.index(1)
    return False, index_of
