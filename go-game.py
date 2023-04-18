print("radio sraka")
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

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
        #draw black knot
        canvas.create_line(self.x*20 + 10, self.y*20, self.x*20 + 10, (self.y + 1)*20, fill='#000000')
        canvas.create_line(self.x*20, self.y*20 + 10, self.x*20 + 20, self.y*20 + 10, fill='#000000')
        

        #draw connections
        for i in range(0, len(self.dots_connected)):
            if self.dots_connected[i].x == self.x - 1 and self.dots_connected[i].y == self.y - 1:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20, self.y*20, fill=self.team.colour)#*
                                                                                                               # @
                                                                                                               #
                
            elif self.dots_connected[i].x == self.x and self.dots_connected[i].y == self.y - 1:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 10, self.y*20, fill=self.team.colour)# *
                                                                                                                    # @
                                                                                                                    #
            
            elif self.dots_connected[i].x == self.x + 1 and self.dots_connected[i].y == self.y - 1:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 20, self.y*20, fill=self.team.colour)#  *
                                                                                                                    # @
                                                                                                                    #

            elif self.dots_connected[i].x == self.x + 1 and self.dots_connected[i].y == self.y:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 20, self.y*20 + 10, fill=self.team.colour)#
                                                                                                                         # @*
                                                                                                                         #

            elif self.dots_connected[i].x == self.x + 1 and self.dots_connected[i].y == self.y + 1:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 20, self.y*20 + 20, fill=self.team.colour)#
                                                                                                                         # @
                                                                                                                         #  *

            elif self.dots_connected[i].x == self.x and self.dots_connected[i].y == self.y + 1:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 10, self.y*20 + 20, fill=self.team.colour)#
                                                                                                                         # @
                                                                                                                         # *

            elif self.dots_connected[i].x == self.x - 1 and self.dots_connected[i].y == self.y + 1:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20, self.y*20 + 20, fill=self.team.colour)#
                                                                                                                    # @
                                                                                                                    #*

            elif self.dots_connected[i].x == self.x - 1 and self.dots_connected[i].y == self.y:
                canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20, self.y*20 + 10, fill=self.team.colour)#
                                                                                                                    #*@
                                                                                                                    #

        #draw dot
        canvas.create_rectangle(self.x*20 + 7, self.y*20 + 7, self.x*20 + 13, self.y*20 + 13, fill=self.team.colour, outline=self.team.colour)
        tk.update()
            
            
            
            
            
            
                
            

        


        

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






number_of_players = 6#int(input("number of players: "))

players = [Player('#ff0000', 0), Player('#00ff00', 0), Player('#0000ff', 0), Player('#bbbb00', 0), Player('#117733', 0), Player('#999999', 0)]
n_players = []
for i in range(0, number_of_players):
    n_players.append(players[i])
players = n_players


size_of_board = 20
board = []
for i in range(0, size_of_board):
    row = []
    for j in range(0, size_of_board):
        dot = Dot(i, j, players[j % 6], [])
        row.append(dot)

    board.append(row)



board[0][0].team = players[0]
board[1][1].dots_connected = [board[0][0], board[1][0], board[2][0], board[2][1], board[2][2], board[1][2], board[0][2], board[0][1]]
for i in range(0, size_of_board):
    for j in range(0, size_of_board):    
        board[i][j].update()
