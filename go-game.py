print("radio sraka")

#create two-dimmensional array of objects that represent dots

class Dot:
    def __init__(self, xcoordinate, ycoordinate, team, dots_connected):
        self.x = xcoordinate
        self.y = ycoordinate
        self.team = team
        self.dots_connected = dots_connected

    def printme(self):
        print("coordinates: ")
        print(str(self.x) + ' ' + str(self.y))
        print("team: ")
        print(self.team)
        print("connections: ")
        print(self.dots_connected)

    def update(self):
        pass

    def check_for_position_acceptance(self):
        pass

    def check_for_connection_with(self, fellow_dot):
        pass

    def check_for_connection_possibility(self):
        pass
        #return boolean

    def make_connection(self):
        pass




class Player:
    def __init__(self, colour, area):
        self.colour = colour
        self.area = area

    def show_area(self):
        pass




size_of_board = 20
board = []
for i in range(0, size_of_board):
    row = []
    for j in range(0, size_of_board):
        dot = Dot(i, j, None, [])
        row.append(dot)

    board.append(row)


