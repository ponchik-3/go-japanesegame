from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

import os
import time
#os.system('cls')


class Dot:
    def __init__(self, xcoordinate, ycoordinate, team, dots_connected):
        self.x = xcoordinate
        self.y = ycoordinate
        self.team = team
        self.dots_connected = dots_connected

    def printme(self):
        #print("coordinates: ")
        print('x:' + str(self.x) + ' ' + 'y:' + str(self.y))
        #print("team: ")
        #print(self.team.colour)
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
        if x < size_of_board - 1 and y > 0:
            if board[x + 1][y - 1].team == self.team and board[x][y - 1].check_for_connection_with(board[x + 1][y]) == False:#  *
                neighbours.append(board[x + 1][y - 1])                                                                       # @
                                                                                                                             #
        if x < size_of_board - 1:
            if board[x + 1][y].team == self.team: #
                neighbours.append(board[x + 1][y])# @*
                                                  #
        if x < size_of_board - 1 and y < size_of_board - 1:
            if board[x + 1][y + 1].team == self.team and board[x + 1][y].check_for_connection_with(board[x][y + 1]) == False:#
                neighbours.append(board[x + 1][y + 1])                                                                       # @
                                                                                                                             #  *
        if y < size_of_board - 1:
            if board[x][y + 1].team == self.team: #
                neighbours.append(board[x][y + 1])# @
                                                  # *
        if x > 0 and y < size_of_board - 1:
            if board[x - 1][y + 1].team == self.team and board[x][y + 1].check_for_connection_with(board[x - 1][y]) == False:#
                neighbours.append(board[x - 1][y + 1])                                                                       # @
                                                                                                                             #*
        if x > 0:
            if board[x - 1][y].team == self.team: #
                neighbours.append(board[x - 1][y])#*@
                                                  #
        return neighbours


    def ist_an_der_grenze(self):
        if self.x == 0 or self.x == size_of_board - 1 or self.y == 0 or self.y == size_of_board - 1:
            return True
        return False


    def connection_possibility(self):
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        matrix[self.x][self.y] = True

        connections = []

        def suchen(current):
            #print('new check')
            #for i in range(0, len(connections)):
             #   print('new con')
              #  connections[i][0].printme()
               # connections[i][1].printme()
            

            neighbours = current.get_accessible_neighbours()
            besonderer_fall = current.ist_an_der_grenze() and self.ist_an_der_grenze() and not(current.x == self.x) and not(current.y == self.y)


            for i in range(0, len(neighbours)):
                if neighbours[i].check_for_connection_with(current) == True:
                    connections.append([current, neighbours[i]])

                
                if (neighbours[i].x == self.x and neighbours[i].y == self.y) or besonderer_fall:
                    conn1 = False
                    conn2 = False
                    for j in range(0, len(connections)):
                        if connections[j][0].x == self.x and connections[j][0].y == self.y:
                            if connections[j][1].x == current.x and connections[j][1].y == current.y:
                                conn1 = True
                        if connections[j][0].x == current.x and connections[j][0].y == current.y:
                            if connections[j][1].x == self.x and connections[j][1].y == self.y:
                                conn2 = True
                    
                    #print(conn1)
                    #print(conn2)
                    if conn1 == False and conn2 == False:
                        connections.append([self, current])
                        if besonderer_fall:
                            self.printme()
                            current.printme()
                            self.team.find_connections(self, current)
                            print('hat an der grenze gefunden')
                        else:
                            self.team.find_connections(self, current)
                            print('found')
                
                if matrix[neighbours[i].x][neighbours[i].y] == False:
                    matrix[neighbours[i].x][neighbours[i].y] = True
                    connections.append([current, neighbours[i]])
                    suchen(neighbours[i])
        
        suchen(self)

                        
            
            
    
    
    
    
    




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
        connections_borders = []
        
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
    def __init__(self, colour, area_chart, interface_colour, interface_height):
        self.colour = colour
        self.area = area_chart
        self.interface_colour = interface_colour
        self.interface_height = interface_height



    def wave_for_area(self, array_matrix, xcrdnt, ycrdnt):
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        matrix[xcrdnt][ycrdnt] = True
        
        wave = []
        front = [board[xcrdnt][ycrdnt]]
        wave.append(front)
        while len(front) > 0:
            vorbereitung = []
            #print('new front')
            for i in range(0, len(front)):
                x = front[i].x
                y = front[i].y
                #print(str(x) + ' ' + str(y))
                if x > 0 and y > 0:
                    if board[x - 1][y] != self and board[x - 1][y].check_for_connection_with(board[x][y - 1]) == False:
                        if matrix[x - 1][y - 1] == False and board[x - 1][y - 1].team != self:
                            vorbereitung.append(board[x - 1][y - 1])
                            matrix[x - 1][y - 1] = True
                
                if y > 0:
                    if not(board[x][y - 1].team == self):
                        if matrix[x][y - 1] == False:
                            vorbereitung.append(board[x][y - 1])
                            matrix[x][y - 1] = True
                
                if x < size_of_board - 1 and y > 0:
                    if board[x + 1][y] != self and board[x + 1][y].check_for_connection_with(board[x][y - 1]) == False:
                        if matrix[x + 1][y - 1] == False and board[x + 1][y - 1].team != self:
                            vorbereitung.append(board[x + 1][y - 1])
                            matrix[x + 1][y - 1] = True
                
                if x < size_of_board - 1:
                    if not(board[x + 1][y].team == self):
                        if matrix[x + 1][y] == False:
                            vorbereitung.append(board[x + 1][y])
                            matrix[x + 1][y] = True
                
                if x < size_of_board - 1 and y < size_of_board - 1:
                    if board[x + 1][y] != self and board[x + 1][y].check_for_connection_with(board[x][y + 1]) == False:
                        if matrix[x + 1][y + 1] == False and board[x + 1][y + 1].team != self:
                            vorbereitung.append(board[x + 1][y + 1])
                            matrix[x + 1][y + 1] = True
                
                if y < size_of_board - 1:
                    if not(board[x][y + 1].team == self):
                        if matrix[x][y + 1] == False:
                            vorbereitung.append(board[x][y + 1])
                            matrix[x][y + 1] = True
                
                if x > 0 and y < size_of_board - 1:
                    if board[x - 1][y] != self and board[x - 1][y].check_for_connection_with(board[x][y + 1]) == False:
                        if matrix[x - 1][y + 1] == False and board[x - 1][y + 1].team != self:
                            vorbereitung.append(board[x - 1][y + 1])
                            matrix[x - 1][y + 1] = True
                
                if x > 0:
                    if not(board[x - 1][y].team == self):
                        if matrix[x - 1][y] == False:
                            vorbereitung.append(board[x - 1][y])
                            matrix[x - 1][y] = True

            
            front = vorbereitung
            wave.append(front)

        sides = 0
        for i in range(0, len(wave)):
            for j in range(0, len(wave[i])):
                if (wave[i][j].x == 0 or wave[i][j].x == size_of_board - 1) or (wave[i][j].y == 0 or wave[i][j].y == size_of_board - 1):
                    sides += 1
        
        #print(sides)
        area = 0
        for i in range(0, len(wave)):
            for j in range(0, len(wave[i])):
                array_matrix[wave[i][j].x][wave[i][j].y] = True

        if sides < size_of_board*2:
            
            for i in range(0, len(wave)):
                area += len(wave[i])
                
        #print(area)
        return area

    
    def get_area(self): 
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        
        area = 0
        i = 0
        j = 0
        while i < size_of_board and j < size_of_board:
            #print(str(i) + str(j))
            if matrix[i][j] == False and board[i][j].team != self:
                
                area += self.wave_for_area(matrix, i, j)
            
            if j == size_of_board - 1:
                j = 0
                i += 1
            else:
                j += 1
        
        #print(area)
        self.area = area



    def show_area(self):
        value = self.area
        

        canvas.create_rectangle(0, self.interface_height + (1 + size_of_board)*20, 500, self.interface_height + (2 + size_of_board)*20, fill='#f0f0f0', outline='#f0f0f0')
        text = 'area circled by player %s: ' % self.interface_colour + str(value)
        canvas.create_text(5, size_of_board*20 + 20 + self.interface_height, text=text, fill='#000000', font=('Courier', 10), anchor='nw')




    def make_connections(self, path):
        for i in range(0, len(path) - 1):
            path[i].dots_connected.append(path[i + 1])
            path[i + 1].dots_connected.append(path[i])
            
            
        path[len(path) - 1].dots_connected.append(path[0])
        path[0].dots_connected.append(path[len(path) - 1])
        
        
        for i in range(0, len(path)):
            path[i].update()

        self.get_area()
        self.show_area()
        


    def find_connections(self, start, finish):
        #work on either case, that is, if the ends are on the border or not
                                                                                                                                                                        #at this point i doubt that my code is the most efficient or readable
                                                                                                                                                                        #but my apologies, i tried my best
        if start.ist_an_der_grenze() and finish.ist_an_der_grenze():
            conn_pretendents = []#for connection cases when borders are involved
            #start.printme()
            #finish.printme()
            matrix = []
            for i in range(0, size_of_board):
                row = []
                for j in range(0, size_of_board):
                    row.append(False)
                matrix.append(row)
            matrix[start.x][start.y] = True
            #matrix[finish.x][finish.y] = True

            wird_enden = False
            while wird_enden == False:
                path = [start]
                
                while True:
                    current = path[len(path) - 1]

                    to_fineesh_da_luup_up = False

                    neighbours = current.get_accessible_neighbours()
                    i = 0
                    while len(neighbours) > i:

                        if neighbours[i].x == finish.x and neighbours[i].y == finish.y:
                            conn_pretendents.append(path)
                            to_fineesh_da_luup_up = True
                            break

                        if matrix[neighbours[i].x][neighbours[i].y] == False:
                            matrix[neighbours[i].x][neighbours[i].y] = True
                            path.append(neighbours[i])
                            break
                        i += 1
                    if i == len(neighbours) or to_fineesh_da_luup_up:
                        #wird_enden = True
                        break
                print('new path')
                for i in range(0, len(path)):
                    path[i].printme()
                
                if path == [start]:
                    wird_enden = True
            
            maxlen = 0
            maxindex = -1
            for i in range(0, len(conn_pretendents)):
                if len(conn_pretendents[i]) > maxlen:
                    maxindex = i
                    maxlen = len(conn_pretendents[i])
        
            self.make_connections(conn_pretendents[maxindex])


                            



        else:
            #depth first search
            #iterate through all possiple paths
            #choose one that goes from start to finish and is the longest


            #print('start and finish')
            #start.printme()
            #finish.printme()
            #print('connections pretendents')
        
        
        
            connections_pretendents = []
        
       
            matrix = []
            for i in range(0, size_of_board):
                row = []
                for j in range(0, size_of_board):
                    row.append(False)
                matrix.append(row)
            matrix[start.x][start.y] = True
            matrix[finish.x][finish.y] = True

            connections = []

            def keinenamenahnungen(path):
                current = path[len(path) - 1]

                neighbours = current.get_accessible_neighbours()
                for i in range(0, len(neighbours)):
                    if neighbours[i].check_for_connection_with(current) == True:
                        connections.append([current, neighbours[i]])

                    if neighbours[i].x == finish.x and neighbours[i].y == finish.y:
                        for j in range(0, len(connections)):
                            conn1 = False#conn1 and conn2 are just stupid variable names, the variables themselves 
                            conn2 = False#are used to check if connections contain (current and finish) pair
                            if connections[j][0].x == current.x and connections[j][0].y == current.y:
                                if connections[j][1].x == finish.x and connections[j][1].y == finish.y:
                                    conn1 = True
                            if connections[j][0].x == finish.x and connections[j][0].y == finish.y:
                                if connections[j][1].x == current.x and connections[j][1].y == current.y:
                                    conn2 = True

                        if conn1 == False and conn2 == False:
                            connections_pretendents.append(path)
                            return
                    

                    if matrix[neighbours[i].x][neighbours[i].y] == False:
                        matrix[neighbours[i].x][neighbours[i].y] = True
                        connections.append([current, neighbours[i]])
                        new_path = path
                        new_path.append(neighbours[i])
                        keinenamenahnungen(new_path)
                    
        
            keinenamenahnungen([start])
        
            for i in range(0, len(connections_pretendents)):
                connections_pretendents[i].append(finish)
            

            maxlen = 0
            maxindex = -1
            for i in range(0, len(connections_pretendents)):
                #print('new connection')
                #for j in range(0, len(connections_pretendents[i])):
                 #   connections_pretendents[i][j].printme()

                if len(connections_pretendents[i]) > maxlen:
                    maxindex = i
                    maxlen = len(connections_pretendents[i])
        
            self.make_connections(connections_pretendents[maxindex])


       



            



    def are_connections_possible(self, start):
        #wave walkthrough
        #create a list of all potentially accessible dots from start
        #then complete another wave walkthrough for each
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)

        wave = []
        front = [start]
        wave.append(front)
        matrix[start.x][start.y] = True

        while len(front) > 0:
            vorbereitung = []
            for i in range(0, len(front)):
                neighbours = front[i].get_accessible_neighbours()

                for j in range(0, len(neighbours)):
                    if matrix[neighbours[j].x][neighbours[j].y] == False:
                        vorbereitung.append(board[neighbours[j].x][neighbours[j].y])
                        matrix[neighbours[j].x][neighbours[j].y] = True

            front = vorbereitung
            wave.append(front)


        for i in range(0, len(wave)):
            for j in range(0, len(wave[i])):
                wave[i][j].connection_possibility()
                                    


            
                



    def put_dot(self):
        dot = Temporary_dot(-1, -1)
        response = '-'

        x = -1
        y = -1
        while response == '-' or check_for_position_acceptance(x, y) == False:
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
            print('if you are sure, press "enter", else type "-"')
            print('if you want to quit the game, type "quit"')
            response = input('')
            if response == 'quit':
                return 'schmetterling'
            
            while response != '' and response != '-':
                print('you have to press "enter" or type "-"')
                print('validate your dot')
                print('if you are sure, press "enter", else type "-"')
                print('if you want to quit the game, type "quit"')
                response = input('')
                if response == 'quit':
                    return 'schmetterling'


        time_spent = time.time()
        dot.move(-1, -1)
        board[x][y] = Dot(x, y, self, [])
        board[x][y].update()
        self.are_connections_possible(board[x][y])
        time_spent = time.time() - time_spent
        global process_time
        print('time spent: %s' % time_spent)
        
        process_time += time_spent
        return 'ja ja arbeit arbeit'





number_of_players = 2#int(input("number of players: "))

#create two-dimmensional array of objects that represent dots
global size_of_board
size_of_board = 20
global board
board = []
global process_time
process_time = 0
operations = 0

for i in range(0, size_of_board):
    row = []
    for j in range(0, size_of_board):
        dot = Dot(i, j, None, [])
        row.append(dot)

    board.append(row)




players = [Player('#ff0000', 0, 'red', 0), Player('#00ff00', 0, 'green', 20), Player('#0000ff', 0, 'blue', 40), 
           Player('#bbbb00', 0, 'golden', 50),
           Player('#117733', 0, 'nocolouridea', 60), Player('#999999', 0, 'silver', 70)]


n_players = []
for i in range(0, number_of_players):
    n_players.append(players[i])
players = n_players


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

#players[0].are_connections_possible(board[2][0])
#print('so long')

#print(board[0][0].ist_an_der_grenze())
#print(board[0][6].ist_an_der_grenze())
#print(board[9][19].ist_an_der_grenze())
#print(board[7][6].ist_an_der_grenze())

players[0].show_area()
players[1].show_area()
#players[0].get_area()
#players[1].put_dot()
#time.sleep(3)

is_procrastinating_with_homework = False
while is_procrastinating_with_homework == False:
    for i in range(0, len(players)):
        operations += 1
        if players[i].put_dot() == 'schmetterling':
            is_procrastinating_with_homework = True
            break
        #else:
            #os.system('cls')
print('Overall processor time: %s' % process_time)
print('Average processor time per an operation: %s' % str(process_time/operations))

if process_time/operations < 1:
    print('well done programmer, well done computer')
