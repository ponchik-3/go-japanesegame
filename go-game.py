
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

        if self.team == None:
            #erase previous
            canvas.create_rectangle(self.x*20, self.y*20, self.x*20 + 20, self.y*20 + 20, fill='#ffffff', outline='#ffffff')
        
            #draw black knot
            canvas.create_line(self.x*20 + 10, self.y*20, self.x*20 + 10, (self.y + 1)*20, fill='#000000')
            canvas.create_line(self.x*20, self.y*20 + 10, self.x*20 + 20, self.y*20 + 10, fill='#000000')

        else:
            #erase previous
            canvas.create_rectangle(self.x*20, self.y*20, self.x*20 + 20, self.y*20 + 20, fill='#ffffff', outline='#ffffff')
        
            #draw black knot
            canvas.create_line(self.x*20 + 10, self.y*20, self.x*20 + 10, (self.y + 1)*20, fill='#000000')
            canvas.create_line(self.x*20, self.y*20 + 10, self.x*20 + 20, self.y*20 + 10, fill='#000000')
        

            #draw connections
            for i in range(0, len(self.dots_connected)):
                if self.dots_connected[i].x == self.x - 1 and self.dots_connected[i].y == self.y - 1:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20, self.y*20, fill=self.team.colour, width=2)#*
                                                                                                                            # @
                                                                                                                            #
                
                elif self.dots_connected[i].x == self.x and self.dots_connected[i].y == self.y - 1:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 10, self.y*20, fill=self.team.colour, width=2)# *
                                                                                                                                 # @
                                                                                                                                 #
            
                elif self.dots_connected[i].x == self.x + 1 and self.dots_connected[i].y == self.y - 1:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 20, self.y*20, fill=self.team.colour, width=2)#  *
                                                                                                                                 # @
                                                                                                                                 #

                elif self.dots_connected[i].x == self.x + 1 and self.dots_connected[i].y == self.y:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 20, self.y*20 + 10, fill=self.team.colour, width=2)#
                                                                                                                                      # @*
                                                                                                                                      #

                elif self.dots_connected[i].x == self.x + 1 and self.dots_connected[i].y == self.y + 1:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 20, self.y*20 + 20, fill=self.team.colour, width=2)#
                                                                                                                                      # @
                                                                                                                                      #  *
                                                                                                                             
                elif self.dots_connected[i].x == self.x and self.dots_connected[i].y == self.y + 1:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20 + 10, self.y*20 + 20, fill=self.team.colour, width=2)#
                                                                                                                                      # @
                                                                                                                                      # *

                elif self.dots_connected[i].x == self.x - 1 and self.dots_connected[i].y == self.y + 1:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20, self.y*20 + 20, fill=self.team.colour, width=2)#
                                                                                                                                 # @
                                                                                                                                 #*

                elif self.dots_connected[i].x == self.x - 1 and self.dots_connected[i].y == self.y:
                    canvas.create_line(self.x*20 + 10, self.y*20 + 10, self.x*20, self.y*20 + 10, fill=self.team.colour, width=2)#
                                                                                                                                 #*@
                                                                                                                                 #

            #draw dot
            canvas.create_rectangle(self.x*20 + 7, self.y*20 + 7, self.x*20 + 14, self.y*20 + 14, fill=self.team.colour, outline=self.team.colour)
            tk.update()
            
        

    def check_for_connection_with(self, fellow_dot):
        if self.team == fellow_dot.team:
            for i in range(0, len(self.dots_connected)):
                if self.dots_connected[i] == fellow_dot:
                    return True
        return False

    
    def is_corner(self):
        if self.x == 0 and self.y == 0:
            return True
        elif self.x == 0 and self.y == size_of_board - 1:
            return True
        elif self.x == size_of_board - 1 and self.y == size_of_board - 1:
            return True
        elif self.x == size_of_board - 1 and self.y == 0:
            return True
        else:
            return False
    
    
    def make_connection_with(self, fellow_dot):
        pass



class Temporary_dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        board[self.x][self.y].update()
        
        self.x = x
        self.y = y
        
        #erase previous
        canvas.create_rectangle(self.x*20, self.y*20, self.x*20 + 20, self.y*20 + 20, fill='#ffffff', outline='#ffffff')

        #draw black knot
        canvas.create_line(self.x*20 + 10, self.y*20, self.x*20 + 10, (self.y + 1)*20, fill='#000000')
        canvas.create_line(self.x*20, self.y*20 + 10, self.x*20 + 20, self.y*20 + 10, fill='#000000')

        #draw dot
        canvas.create_line(self.x*20 + 7, self.y*20 + 7, self.x*20 + 14, self.y*20 + 14, fill='#000000')
        canvas.create_line(self.x*20 + 7, self.y*20 + 14, self.x*20 + 14, self.y*20 + 7, fill='#000000')
        
        tk.update()
        



def check_for_position_acceptance(x, y):
        if x < 0 or x > size_of_board - 1 or y < 0 or y > size_of_board - 1:
            return False
        if board[x][y].team != None:
            return False 
        
        #wave walkthrough
        #will determine if the placement is acceptable by counting accessible corners
        corners = 0
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for i in range(0, size_of_board):
                row.append(False)
            matrix.append(row)

        front = [board[x][y]]
        
        
        while len(front) > 0:
            next_front = []
            for i in range(0, len(front)):
                currentx = front[i].x
                currenty = front[i].y

                if currenty > 0:#the wave cannot spread onto the other dot, as well as cross the connection between two other dots
                    if board[currentx][currenty - 1].team == None and matrix[currentx][currenty - 1] == False:# *
                        next_front.append(board[currentx][currenty - 1])                                      # @
                        matrix[currentx][currenty - 1] = True                                                 #
                        

                if currentx < size_of_board - 1:
                    if board[currentx + 1][currenty].team == None and matrix[currentx + 1][currenty] == False:#
                        next_front.append(board[currentx + 1][currenty])                                      # @*
                        matrix[currentx + 1][currenty] = True                                                 #
                        
                        
                if currenty < size_of_board - 1:
                    if board[currentx][currenty + 1].team == None and matrix[currentx][currenty + 1] == False:#
                        next_front.append(board[currentx][currenty + 1])                                      # @
                        matrix[currentx][currenty + 1] = True                                                 # *
                        
                        
                if currentx > 0:
                    if board[currentx - 1][currenty].team == None and matrix[currentx - 1][currenty] == False:#
                        next_front.append(board[currentx - 1][currenty])                                      #*@
                        matrix[currentx - 1][currenty] = True                                                 #
                        


                if currentx > 0 and currenty > 0:
                    if board[currentx - 1][currenty - 1].team == None and matrix[currentx - 1][currenty - 1] == False:#*
                        if board[currentx - 1][currenty].check_for_connection_with(board[currentx][currenty - 1]) == False:    # @
                            next_front.append(board[currentx - 1][currenty - 1])                                      #
                            matrix[currentx - 1][currenty - 1] = True
                            

                if currentx < size_of_board - 1 and currenty > 0:
                    if board[currentx + 1][currenty - 1].team == None and matrix[currentx + 1][currenty - 1] == False:#  *
                        if board[currentx][currenty - 1].check_for_connection_with(board[currentx + 1][currenty]) == False:    # @
                            next_front.append(board[currentx + 1][currenty - 1])                                      #
                            matrix[currentx + 1][currenty - 1] = True
                            

                if currentx < size_of_board - 1 and currenty < size_of_board - 1:
                    if board[currentx + 1][currenty + 1].team == None and matrix[currentx + 1][currenty + 1] == False:#
                        if board[currentx + 1][currenty].check_for_connection_with(board[currentx][currenty + 1]) == False:    # @
                            next_front.append(board[currentx + 1][currenty + 1])                                      #  *
                            matrix[currentx + 1][currenty + 1] = True
                            

                if currentx > 0 and currenty < size_of_board - 1:
                    if board[currentx - 1][currenty + 1].team == None and matrix[currentx - 1][currenty + 1] == False:#
                        if board[currentx][currenty + 1].check_for_connection_with(board[currentx - 1][currenty]) == False:    # @
                            next_front.append(board[currentx - 1][currenty + 1])                                      #*
                            matrix[currentx - 1][currenty + 1] = True
                            

            front = next_front
            
        if matrix[0][0] == True:
            corners += 1
        if matrix[0][size_of_board - 1] == True:
            corners += 1
        if matrix[size_of_board - 1][0] == True:
            corners += 1
        if matrix[size_of_board - 1][size_of_board - 1] == True:
            corners += 1
        print(corners)
        if corners > 1:
            return True
        else:
            return False
        
             
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



    def make_connections(self, path):
        pass


    def find_connections(self, path):
        dot = path[len(path) - 1]
        potential_connections = dot.dots_connected
        if dot.x > 0 and dot.y > 0:
            if board[dot.x - 1][dot.y - 1].team == self:
                potential_connections.append(board[dot.x - 1][dot.y - 1])

        if dot.y > 0:
            if board[dot.x][dot.y - 1].team == self:
                potential_connections.append(board[dot.x][dot.y - 1])

        if dot.x < size_of_board - 1 and dot.y > 0:
            if board[dot.x + 1][dot.y - 1].team == self:
                potential_connections.append(board[dot.x + 1][dot.y - 1])

        if dot.x < size_of_board - 1:
            if board[dot.x + 1][dot.y].team == self:
                potential_connections.append(board[dot.x + 1][dot.y])

        if dot.x < size_of_board - 1 and dot.y < size_of_board - 1:
            if board[dot.x + 1][dot.y + 1].team == self:
                potential_connections.append(board[dot.x + 1][dot.y + 1])

        if dot.y < size_of_board - 1:
            if board[dot.x][dot.y + 1].team == self:
                potential_connections.append(board[dot.x][dot.y + 1])

        if dot.x > 0 and dot.y < size_of_board - 1:
            if board[dot.x - 1][dot.y + 1].team == self:
                potential_connections.append(board[dot.x - 1][dot.y + 1])

        if dot.x > 0:
            if board[dot.x - 1][dot.y].team == self:
                potential_connections.append(board[dot.x - 1][dot.y])



        for i in range(0, len(potential_connections)):
            if potential_connections[i] == path[0]:
                self.make_connections(path)
            else:
                new_path = path
                new_path.append(potential_connections[i])
                find_connections(new_path)

    



    def put_dot(self):
        dot = Temporary_dot(-1, -1)
        response = 'no'

        x = -1
        y = -1
        while response == 'no' or check_for_position_acceptance(x, y) == False:
            print("write the coordinates where you want to place the dot")
            x = int(input('x: '))
            y = int(input('y: '))
            
    
            while check_for_position_acceptance(x, y) == False:
                print('enter value following the rules')
                x = int(input('x: '))
                y = int(input('y: '))

            dot.move(x, y)
            
            print('validate your dot')
            print('if you are sure, type "yes", else type "no"')
            response = input('')
            
            while response != 'yes' and response != 'no':
                print('you have to type "yes" or "no"')
                print('validate your dot')
                print('if you are sure, type "yes", else type "no"')
                response = input('')

        dot.move(-1, -1)
        board[x][y] = Dot(x, y, self, [])
        board[x][y].update()

        
        






number_of_players = 6#int(input("number of players: "))

players = [Player('#ff0000', 0), Player('#00ff00', 0), Player('#0000ff', 0), Player('#bbbb00', 0), Player('#117733', 0), Player('#999999', 0)]
n_players = []
for i in range(0, number_of_players):
    n_players.append(players[i])
players = n_players



global size_of_board
size_of_board = 20
global board
board = []

for i in range(0, size_of_board):
    row = []
    for j in range(0, size_of_board):
        dot = Dot(i, j, None, [])

size_of_board = 20
board = []
for i in range(0, size_of_board):
    row = []
    for j in range(0, size_of_board):
        dot = Dot(i, j, players[j % 6], [])

        row.append(dot)

    board.append(row)



board[0][0].team = players[0]

board[0][1].team = players[0]
board[1][2].team = players[0]
board[2][1].team = players[0]
board[1][0].team = players[0]

board[0][0].dots_connected = [board[0][1], board[1][0]]
board[0][1].dots_connected = [board[0][0], board[1][2]]
board[1][2].dots_connected = [board[0][1], board[2][1]]
board[2][1].dots_connected = [board[1][2], board[1][0]]
board[1][0].dots_connected = [board[2][1], board[0][0]]

#board[1][1].dots_connected = [board[0][0], board[1][0], board[2][0], board[2][1], board[2][2], board[1][2], board[0][2], board[0][1]]
for i in range(0, size_of_board):
    for j in range(0, size_of_board):    
        board[i][j].update()

players[1].put_dot()

#while True:
 #   for i in range(0, len(players)):
  #      players[i].put_dot()

board[1][1].dots_connected = [board[0][0], board[1][0], board[2][0], board[2][1], board[2][2], board[1][2], board[0][2], board[0][1]]
for i in range(0, size_of_board):
    for j in range(0, size_of_board):    
        board[i][j].update()

