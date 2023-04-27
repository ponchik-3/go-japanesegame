from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

import time

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
        print(self.team.colour)
        #print("connections: ")
        #print(self.dots_connected)
        print("")

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
    


    def get_accessible_neighbours(self):
        neighbours = []
        x = self.x
        y = self.y
        if x > 0 and y > 0:
            if board[x - 1][y - 1].team == self.team and board[x - 1][y].check_for_connection_with(board[x][y - 1]) == False:#*
                neighbours.append(board[x - 1][y - 1])                                                                       # @
                                                                                                                             #
        if y > 0:
            if board[x][y - 1].team == self.team: # *
                neighbours.append(board[x][y - 1])# @
                                                  #
        if x < size_of_board and y > 0:
            if board[x + 1][y - 1].team == self.team and board[x][y - 1].check_for_connection_with(board[x + 1][y]) == False:#  *
                neighbours.append(board[x + 1][y - 1])                                                                       # @
                                                                                                                             #
        if x < size_of_board:
            if board[x + 1][y].team == self.team: #
                neighbours.append(board[x + 1][y])# @*
                                                  #
        if x < size_of_board and y < size_of_board:
            if board[x + 1][y + 1].team == self.team and board[x + 1][y].check_for_connection_with(board[x][y + 1]) == False:#
                neighbours.append(board[x + 1][y + 1])                                                                       # @
                                                                                                                             #  *
        if y < size_of_board:
            if board[x][y + 1].team == self.team: #
                neighbours.append(board[x][y + 1])# @
                                                  # *
        if x > 0 and y < size_of_board:
            if board[x - 1][y + 1].team == self.team and board[x][y + 1].check_for_connection_with(board[x - 1][y]) == False:#
                neighbours.append(board[x - 1][y + 1])                                                                       # @
                                                                                                                             #*
        if x > 0:
            if board[x - 1][y].team == self.team: #
                neighbours.append(board[x - 1][y])#*@
                                                  #
        return neighbours


    
    
    
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
        #will determine if the placement is acceptable by counting accessible side knots
        sides = 0
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
                    if board[currentx - 1][currenty - 1].team == None and matrix[currentx - 1][currenty - 1] == False:         #*
                        if board[currentx - 1][currenty].check_for_connection_with(board[currentx][currenty - 1]) == False:    # @
                            next_front.append(board[currentx - 1][currenty - 1])                                               #
                            matrix[currentx - 1][currenty - 1] = True
                            

                if currentx < size_of_board - 1 and currenty > 0:
                    if board[currentx + 1][currenty - 1].team == None and matrix[currentx + 1][currenty - 1] == False:         #  *
                        if board[currentx][currenty - 1].check_for_connection_with(board[currentx + 1][currenty]) == False:    # @
                            next_front.append(board[currentx + 1][currenty - 1])                                               #
                            matrix[currentx + 1][currenty - 1] = True
                            

                if currentx < size_of_board - 1 and currenty < size_of_board - 1:
                    if board[currentx + 1][currenty + 1].team == None and matrix[currentx + 1][currenty + 1] == False:         #
                        if board[currentx + 1][currenty].check_for_connection_with(board[currentx][currenty + 1]) == False:    # @
                            next_front.append(board[currentx + 1][currenty + 1])                                               #  *
                            matrix[currentx + 1][currenty + 1] = True
                            

                if currentx > 0 and currenty < size_of_board - 1:
                    if board[currentx - 1][currenty + 1].team == None and matrix[currentx - 1][currenty + 1] == False:         #
                        if board[currentx][currenty + 1].check_for_connection_with(board[currentx - 1][currenty]) == False:    # @
                            next_front.append(board[currentx - 1][currenty + 1])                                               #*
                            matrix[currentx - 1][currenty + 1] = True
                            

            front = next_front

        #count the accsesible side knots
        for i in range(0, size_of_board):
            if matrix[0][i] == True:
                sides += 1
            if matrix[i][0] == True:
                sides += 1
            if matrix[size_of_board - 1][i] == True:
                sides += 1
            if matrix[i][size_of_board - 1] == True:
                sides += 1
        #print(sides)
        
        if sides > size_of_board*2:
            return True
        else:
            return False
        
             

def look_for_element(array, element):
    for i in range(1, len(array)):
        if array[i] == element:
            return True
    return False



class Player:
    def __init__(self, colour, area, interface_colour):
        self.colour = colour
        self.area = area
        self.interface_colour = interface_colour

    def show_area(self):
        pass


    def make_connections(self, path):
        for i in range(0, len(path) - 1):
            path[i].dots_connected.append(path[i + 1])
            path[i + 1].dots_connected.append(path[i])
            #path[i].printme()
            
        path[len(path) - 1].dots_connected.append(path[0])
        path[0].dots_connected.append(path[len(path) - 1])
        #path[len(path) - 1].printme()
        
        for i in range(0, len(path)):
            path[i].update()


    def find_connections(self, start, finish):
        #depth first search
        #iterate through all possiple paths
        #choose one that goes from start to finish and is the longest
                                                                                                                                                                        #at this point i doubt that my code is the most efficient or readable
                                                                                                                                                                        #but i don't care
        start.printme()
        finish.printme()
        
        path = []
        
        connections_pretendents = []
        path.append(start)
       
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        matrix[start.x][start.y] = True


        def keinenamenahnungen(path):
            current = path[len(path) - 1]

            neighbours = current.get_accessible_neighbours()
            for i in range(0, len(neighbours)):
                if matrix[neighbours[i].x][neighbours[i].y] == False:
                    if neighbours[i].x == finish.x and neighbours[i].y == finish.y:
                        connections_pretendents.append(path)

                    else:
                        matrix[neighbours[i].x][neighbours[i].y] = True
                        new_path = path
                        new_path.append(neighbours[i])
                        keinenamenahnungen(new_path)
        
        keinenamenahnungen(path)
        for i in range(0, len(connections_pretendents)):
            print('another path')
            connections_pretendents[i].append(finish)
            for j in range(0, len(connections_pretendents[i])):
                connections_pretendents[i][j].printme()

        maxindex = -1
        maxlen = 0
        for i in range(0, len(connections_pretendents)):
            if len(connections_pretendents[i]) > maxlen:
                maxlen = len(connections_pretendents[i])
                maxindex = i
        
        self.make_connections(connections_pretendents[maxindex])


       



            



    def are_connections_possible(self, start):
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)

        
        front = [start]
        matrix[start.x][start.y] = True
        #wave walkthrough
        #connections are possible if the wave will be widenned and then narrowed to one point
        #refactor using .get_accessible_neighbours function
        while len(front) > 0:
            vorbereitung = []

            

            for i in range(0, len(front)):
                if front[i].x > 0 and front[i].y > 0:
                    if matrix[front[i].x - 1][front[i].y - 1] == False and board[front[i].x - 1][front[i].y - 1].team == self:        #*
                        if board[front[i].x][front[i].y - 1].check_for_connection_with(board[front[i].x - 1][front[i].y]) == False:   # @
                            vorbereitung.append(board[front[i].x - 1][front[i].y - 1])                                                #
                            matrix[front[i].x - 1][front[i].y - 1] = True

                if front[i].y > 0:
                    if matrix[front[i].x][front[i].y - 1] == False and board[front[i].x][front[i].y - 1].team == self:# *
                        vorbereitung.append(board[front[i].x][front[i].y - 1])                                        # @
                        matrix[front[i].x][front[i].y - 1] = True                                                     #

                if front[i].x < size_of_board - 1 and front[i].y > 0:
                    if matrix[front[i].x + 1][front[i].y - 1] == False and board[front[i].x + 1][front[i].y - 1].team == self:         #  *
                        if board[front[i].x][front[i].y - 1].check_for_connection_with(board[front[i].x + 1][front[i].y]) == False:    # @
                            vorbereitung.append(board[front[i].x + 1][front[i].y - 1])                                                 #
                            matrix[front[i].x + 1][front[i].y - 1] = True

                if front[i].x < size_of_board - 1:
                    if matrix[front[i].x + 1][front[i].y] == False and board[front[i].x + 1][front[i].y].team == self:#
                        vorbereitung.append(board[front[i].x + 1][front[i].y])                                        # @*
                        matrix[front[i].x + 1][front[i].y] = True                                                     #
            
                if front[i].x < size_of_board - 1 and front[i].y < size_of_board - 1:
                    if matrix[front[i].x + 1][front[i].y + 1] == False and board[front[i].x + 1][front[i].y + 1].team == self:         #
                        if board[front[i].x][front[i].y + 1].check_for_connection_with(board[front[i].x + 1][front[i].y]) == False:    # @
                            vorbereitung.append(board[front[i].x + 1][front[i].y + 1])                                                 #  *
                            matrix[front[i].x + 1][front[i].y + 1] = True

                if front[i].y < size_of_board - 1:
                    if matrix[front[i].x][front[i].y + 1] == False and board[front[i].x][front[i].y + 1].team == self:#
                        vorbereitung.append(board[front[i].x][front[i].y + 1])                                        # @
                        matrix[front[i].x][front[i].y + 1] = True                                                     # *

                if front[i].x > 0 and front[i].y < size_of_board - 1:
                    if matrix[front[i].x - 1][front[i].y + 1] == False and board[front[i].x - 1][front[i].y + 1].team == self:         #
                        if board[front[i].x][front[i].y + 1].check_for_connection_with(board[front[i].x - 1][front[i].y]) == False:    # @
                            vorbereitung.append(board[front[i].x - 1][front[i].y + 1])                                                 #*
                            matrix[front[i].x - 1][front[i].y + 1] = True

                if front[i].x > 0:
                    if matrix[front[i].x - 1][front[i].y] == False and board[front[i].x - 1][front[i].y].team == self:#
                        vorbereitung.append(board[front[i].x - 1][front[i].y])                                        #*@
                        matrix[front[i].x - 1][front[i].y] = True                                                     #
            


            for i in range(0, len(vorbereitung)):
                for j in range(0, len(vorbereitung)):
                    if i != j:
                        if abs(vorbereitung[i].x - vorbereitung[j].x) < 2 and abs(vorbereitung[i].y - vorbereitung[j].y) < 2:
                            if vorbereitung[i].check_for_connection_with(vorbereitung[j]) == False:
                                print('found')
                                self.find_connections(vorbereitung[i], vorbereitung[j])
                                return
                for j in range(0, len(front)):
                    for k in range(0, len(front)):
                        if j != k:
                            if abs(vorbereitung[i].x - front[j].x) < 2 and abs(vorbereitung[i].y - front[j].y) < 2:
                                if abs(vorbereitung[i].x - front[k].x) < 2 and abs(vorbereitung[i].y - front[k].y) < 2:
                                    if vorbereitung[i].check_for_connection_with(front[j]) == False or vorbereitung[i].check_for_connection_with(front[k]) == False:
                                        print('found in other way')
                                        self.find_connections(vorbereitung[i], front[k])
                                        return 
                                    
                        
            
            front = vorbereitung


            
                



    def put_dot(self):
        dot = Temporary_dot(-1, -1)
        response = 'no'

        x = -1
        y = -1
        while response == 'no' or check_for_position_acceptance(x, y) == False:
            print('player ' + self.interface_colour)
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
            print('if you want to quit the game, type "quit"')
            response = input('')
            if response == 'quit':
                return 'schmetterling'
            
            while response != 'yes' and response != 'no':
                print('you have to type "yes" or "no"')
                print('validate your dot')
                print('if you are sure, type "yes", else type "no"')
                print('if you want to quit the game, type "quit"')
                response = input('')
                if response == 'quit':
                    return 'schmetterling'


        dot.move(-1, -1)
        board[x][y] = Dot(x, y, self, [])
        board[x][y].update()
        self.are_connections_possible(board[x][y])
        return 'ja ja arbeit arbeit'





number_of_players = 2#int(input("number of players: "))

players = [Player('#ff0000', 0, 'red'), Player('#00ff00', 0, 'green'), Player('#0000ff', 0, 'blue'), Player('#bbbb00', 0, 'golden'),
            Player('#117733', 0, 'nocolouridea'), Player('#999999', 0, 'silver')]

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
        row.append(dot)

    board.append(row)



#board[0][0].team = players[0]
#board[1][0].team = players[0]
#board[2][0].team = players[0]
#board[3][1].team = players[0]
#board[2][1].team = players[0]
#board[2][2].team = players[0]
#board[1][3].team = players[0]
#board[0][2].team = players[0]
#board[0][1].team = players[0]
#board[1][2].team = players[0]
#board[1][1].team = players[0]

#players[0].make_connections([board[2][2], board[1][1], board[0][2], board[1][3]])

for i in range(0, size_of_board):
    for j in range(0, size_of_board):    
        board[i][j].update()

#players[0].are_connections_possible(board[0][1])


#players[1].put_dot()
#time.sleep(10)
is_procrastinating_with_homework = False
while is_procrastinating_with_homework == False:
    for i in range(0, len(players)):
        if players[i].put_dot() == 'schmetterling':
            is_procrastinating_with_homework = True
            break
