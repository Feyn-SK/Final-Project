from Neighborhood import neighbor as nbh
class state:

    initial_state = 0

    def __init__(self, row, col, parent_array):
        self.state = state.initial_state
        self.row = row
        self.col = col
        self.neighbhorhood = nbh(parent_array,row,col)

    def __eq__(self,other):
        return self.state == other.state

    def setneighbhorhood(self,parent_array, row, col):
        self.neighbhorhood = nbh(parent_array,row,col)


    def getstate(self):
        return self.state

    def setstate(self):
        self.state


