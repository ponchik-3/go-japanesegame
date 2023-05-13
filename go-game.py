from tkinter import *
import os
import time
import random
os.system('cls')

def fffff():
    print('bbb   rrrr     a      i    n   n  fffff  u   u   cccc  k   k')
    print('b  b  r   r   a a     i    nn  n  f      u   u  c      k kk ')
    print('bbb   rrrr   a   a    i    n n n  ffff   u   u  c      kk')
    print('b  b  r rr   aaaaa    i    n  nn  f      u   u  c      k kk ')
    print('bbb   r   r  a   a    i    n   n  f       uuu    cccc  k   k')

random_number = random.randint(0, 99)
if random_number == 0:
    fffff()
    time.sleep(1)
    os.system('cls')


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
    


    def get_accessible_neighbours(self, localboard):
        neighbours = []
        x = self.x
        y = self.y
        if x > 0 and y > 0:
            if localboard[x - 1][y - 1].team == self.team and localboard[x - 1][y].check_for_connection_with(localboard[x][y - 1]) == False:#*
                neighbours.append(localboard[x - 1][y - 1])                                                                                 # @
                                                                                                                                            #
        if y > 0:
            if localboard[x][y - 1].team == self.team: # *
                neighbours.append(localboard[x][y - 1])# @
                                                  #
        if x < size_of_board - 1 and y > 0:
            if localboard[x + 1][y - 1].team == self.team and localboard[x][y - 1].check_for_connection_with(localboard[x + 1][y]) == False:#  *
                neighbours.append(localboard[x + 1][y - 1])                                                                                 # @
                                                                                                                                            #
        if x < size_of_board - 1:
            if localboard[x + 1][y].team == self.team: #
                neighbours.append(localboard[x + 1][y])# @*
                                                  #
        if x < size_of_board - 1 and y < size_of_board - 1:
            if localboard[x + 1][y + 1].team == self.team and localboard[x + 1][y].check_for_connection_with(localboard[x][y + 1]) == False:#
                neighbours.append(localboard[x + 1][y + 1])                                                                                 # @
                                                                                                                                            #  *
        if y < size_of_board - 1:
            if localboard[x][y + 1].team == self.team: #
                neighbours.append(localboard[x][y + 1])# @
                                                  # *
        if x > 0 and y < size_of_board - 1:
            if localboard[x - 1][y + 1].team == self.team and localboard[x][y + 1].check_for_connection_with(localboard[x - 1][y]) == False:#
                neighbours.append(localboard[x - 1][y + 1])                                                                                 # @
                                                                                                                                            #*
        if x > 0:
            if localboard[x - 1][y].team == self.team: #
                neighbours.append(localboard[x - 1][y])#*@
                                                  #
        return neighbours


    def ist_an_der_grenze(self):
        if self.x == 0 or self.x == size_of_board - 1 or self.y == 0 or self.y == size_of_board - 1:
            return True
        return False


    def are_on_the_same_side(self, fellow_dot):
        if self.x == 0 and fellow_dot.x == 0:
            if self.y == 0 and fellow_dot.y == 0:
                return True
            elif self.y == size_of_board - 1 and fellow_dot.y == size_of_board - 1:
                return True
            
        elif self.x == size_of_board - 1 and fellow_dot.x == size_of_board - 1:
            if self.y == 0 and fellow_dot.y == 0:
                return True
            elif self.y == size_of_board - 1 and fellow_dot.y == size_of_board - 1:
                return True
            
        else:
            return False


    def connection_possibility(self, localboard, is_for_real):
        #print('start')
        #self.printme()
        


        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        matrix[self.x][self.y] = True

        connections = []

        def suchen(path):
            current = path[len(path) - 1]

            neighbours = current.get_accessible_neighbours(localboard)
            

            for i in range(0, len(neighbours)):
                if neighbours[i].check_for_connection_with(current) == True:
                    connections.append([current, neighbours[i]])

                
                besonderer_fall = False
                if neighbours[i].ist_an_der_grenze():
                    if self.ist_an_der_grenze():
                        if not(neighbours[i].x == self.x and neighbours[i].y == self.y):    
                            besonderer_fall = True
                

                #if two ends are on different sides, then they automatically can be connected
                #if they are on one side, then we need to check if they are the only dots on side 
                #from all the path
                if besonderer_fall:
                    #for j in range(0, len(path)):
                     #   path[j].printme()



                    if self.are_on_the_same_side(neighbours[i]) == False:
                        #prevent the case where everything is already connected
                        new_path = []
                        for jj in range(0, len(path)):
                            new_path.append(path[jj])
                        new_path.append(neighbours[i])

                        free_neighbours = 0
                        for jj in range(0, len(new_path) - 1):
                            #print(str(jj) + ' ' + str(jj + 1))
                            #print(new_path[jj].check_for_connection_with(new_path[jj + 1]))
                            if new_path[jj].check_for_connection_with(new_path[jj + 1]) == False:
                                free_neighbours += 1
                        

                        if free_neighbours > 0:
                            #print('found on different sides')
                            self.team.find_connections(self, neighbours[i], localboard, is_for_real)
                        


                    else:
                        dots_on_border = 0
                        for j in range(0, len(path)):
                            if path[j].ist_an_der_grenze() == True:
                                dots_on_border += 1
                        
                        if dots_on_border < 2:
                            #still the case when the beginning and the end are neighbours IUKBapuTb MoI-O Dyny
                            special_case = False
                            special_case_neighbours = self.get_accessible_neighbours(localboard)
                            for ii in range(0, len(special_case_neighbours)):
                                if special_case_neighbours[ii].x == neighbours[i].x and special_case_neighbours[ii].y == neighbours[i].y:
                                    special_case = True
                            

                            if special_case == False:
                                new_path = []
                                for jj in range(0, len(path)):
                                    new_path.append(path[jj])
                                new_path.append(neighbours[i])

                                free_neighbours = 0
                                for jj in range(0, len(new_path) - 1):
                                    #print(str(jj) + ' ' + str(jj + 1))
                                    #print(new_path[jj].check_for_connection_with(new_path[jj + 1]))
                                    if new_path[jj].check_for_connection_with(new_path[jj + 1]) == False:
                                        free_neighbours += 1
                        
                        
                                if free_neighbours > 0:
                                    #print('found on the same side')
                                    self.team.find_connections(self, neighbours[i], localboard, is_for_real)
                            #else:
                                #print('y cpaky')
                
                
                if (neighbours[i].x == self.x and neighbours[i].y == self.y):
                    conn1 = False
                    conn2 = False
                    for j in range(0, len(connections)):
                        if connections[j][0].x == self.x and connections[j][0].y == self.y:
                            if connections[j][1].x == current.x and connections[j][1].y == current.y:
                                conn1 = True
                        if connections[j][0].x == current.x and connections[j][0].y == current.y:
                            if connections[j][1].x == self.x and connections[j][1].y == self.y:
                                conn2 = True
                    
                    
                    if conn1 == False and conn2 == False:
                        connections.append([self, current])
                        self.team.find_connections(self, current, localboard, is_for_real)
                        
                
                

                if matrix[neighbours[i].x][neighbours[i].y] == False:
                    matrix[neighbours[i].x][neighbours[i].y] = True
                    connections.append([current, neighbours[i]])

                    new_path = []
                    for j in range(0, len(path)):
                        new_path.append(path[j])
                    new_path.append(neighbours[i])

                    suchen(new_path)
        
        suchen([self])

                        
            
            
    
    
    
    
    




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
        



def check_for_position_acceptance(x, y, localboard):
        if x < 0 or x > size_of_board - 1 or y < 0 or y > size_of_board - 1:
            return False
        if localboard[x][y].team != None:
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

        front = [localboard[x][y]]
        connections_borders = []
        
        while len(front) > 0:
            next_front = []
            for i in range(0, len(front)):
                currentx = front[i].x
                currenty = front[i].y

                if currenty > 0:#the wave cannot spread onto the other dot, as well as cross the connection between two other dots
                    if localboard[currentx][currenty - 1].team == None and matrix[currentx][currenty - 1] == False:# *
                        next_front.append(localboard[currentx][currenty - 1])                                      # @
                        matrix[currentx][currenty - 1] = True                                                 #
                        

                if currentx < size_of_board - 1:
                    if localboard[currentx + 1][currenty].team == None and matrix[currentx + 1][currenty] == False:#
                        next_front.append(localboard[currentx + 1][currenty])                                      # @*
                        matrix[currentx + 1][currenty] = True                                                 #
                        
                        
                if currenty < size_of_board - 1:
                    if localboard[currentx][currenty + 1].team == None and matrix[currentx][currenty + 1] == False:#
                        next_front.append(localboard[currentx][currenty + 1])                                      # @
                        matrix[currentx][currenty + 1] = True                                                 # *
                        
                        
                if currentx > 0:
                    if localboard[currentx - 1][currenty].team == None and matrix[currentx - 1][currenty] == False:#
                        next_front.append(localboard[currentx - 1][currenty])                                      #*@
                        matrix[currentx - 1][currenty] = True                                                 #
                        


                if currentx > 0 and currenty > 0:
                    if localboard[currentx - 1][currenty - 1].team == None and matrix[currentx - 1][currenty - 1] == False:         #*
                        if localboard[currentx - 1][currenty].check_for_connection_with(localboard[currentx][currenty - 1]) == False:    # @
                            next_front.append(localboard[currentx - 1][currenty - 1])                                               #
                            matrix[currentx - 1][currenty - 1] = True
                            

                if currentx < size_of_board - 1 and currenty > 0:
                    if localboard[currentx + 1][currenty - 1].team == None and matrix[currentx + 1][currenty - 1] == False:         #  *
                        if localboard[currentx][currenty - 1].check_for_connection_with(localboard[currentx + 1][currenty]) == False:    # @
                            next_front.append(localboard[currentx + 1][currenty - 1])                                               #
                            matrix[currentx + 1][currenty - 1] = True
                            

                if currentx < size_of_board - 1 and currenty < size_of_board - 1:
                    if localboard[currentx + 1][currenty + 1].team == None and matrix[currentx + 1][currenty + 1] == False:         #
                        if localboard[currentx + 1][currenty].check_for_connection_with(localboard[currentx][currenty + 1]) == False:    # @
                            next_front.append(localboard[currentx + 1][currenty + 1])                                               #  *
                            matrix[currentx + 1][currenty + 1] = True
                            

                if currentx > 0 and currenty < size_of_board - 1:
                    if localboard[currentx - 1][currenty + 1].team == None and matrix[currentx - 1][currenty + 1] == False:         #
                        if localboard[currentx][currenty + 1].check_for_connection_with(localboard[currentx - 1][currenty]) == False:    # @
                            next_front.append(localboard[currentx - 1][currenty + 1])                                               #*
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



    def wave_for_area(self, array_matrix, xcrdnt, ycrdnt, localboard):
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        matrix[xcrdnt][ycrdnt] = True
        
        wave = []
        front = [localboard[xcrdnt][ycrdnt]]
        wave.append(front)
        while len(front) > 0:
            vorbereitung = []
            #print('new front')
            for i in range(0, len(front)):
                x = front[i].x
                y = front[i].y
                #print(str(x) + ' ' + str(y))
                if x > 0 and y > 0:
                    if localboard[x - 1][y] != self and localboard[x - 1][y].check_for_connection_with(localboard[x][y - 1]) == False:
                        if matrix[x - 1][y - 1] == False and localboard[x - 1][y - 1].team != self:
                            vorbereitung.append(localboard[x - 1][y - 1])
                            matrix[x - 1][y - 1] = True
                
                if y > 0:
                    if not(localboard[x][y - 1].team == self):
                        if matrix[x][y - 1] == False:
                            vorbereitung.append(localboard[x][y - 1])
                            matrix[x][y - 1] = True
                
                if x < size_of_board - 1 and y > 0:
                    if localboard[x + 1][y] != self and localboard[x + 1][y].check_for_connection_with(localboard[x][y - 1]) == False:
                        if matrix[x + 1][y - 1] == False and localboard[x + 1][y - 1].team != self:
                            vorbereitung.append(localboard[x + 1][y - 1])
                            matrix[x + 1][y - 1] = True
                
                if x < size_of_board - 1:
                    if not(localboard[x + 1][y].team == self):
                        if matrix[x + 1][y] == False:
                            vorbereitung.append(localboard[x + 1][y])
                            matrix[x + 1][y] = True
                
                if x < size_of_board - 1 and y < size_of_board - 1:
                    if localboard[x + 1][y] != self and localboard[x + 1][y].check_for_connection_with(localboard[x][y + 1]) == False:
                        if matrix[x + 1][y + 1] == False and localboard[x + 1][y + 1].team != self:
                            vorbereitung.append(localboard[x + 1][y + 1])
                            matrix[x + 1][y + 1] = True
                
                if y < size_of_board - 1:
                    if not(localboard[x][y + 1].team == self):
                        if matrix[x][y + 1] == False:
                            vorbereitung.append(localboard[x][y + 1])
                            matrix[x][y + 1] = True
                
                if x > 0 and y < size_of_board - 1:
                    if localboard[x - 1][y] != self and localboard[x - 1][y].check_for_connection_with(localboard[x][y + 1]) == False:
                        if matrix[x - 1][y + 1] == False and localboard[x - 1][y + 1].team != self:
                            vorbereitung.append(localboard[x - 1][y + 1])
                            matrix[x - 1][y + 1] = True
                
                if x > 0:
                    if not(localboard[x - 1][y].team == self):
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

    
    def get_area(self, localboard): 
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
            if matrix[i][j] == False and localboard[i][j].team != self:
                
                area += self.wave_for_area(matrix, i, j, localboard)
            
            if j == size_of_board - 1:
                j = 0
                i += 1
            else:
                j += 1
        
        #print(area)
        return area



    def show_area(self):
        value = self.area
        

        canvas.create_rectangle(0, self.interface_height + (1 + size_of_board)*20, 500, self.interface_height + (2 + size_of_board)*20, fill='#f0f0f0', outline='#f0f0f0')
        text = 'area circled by player %s: ' % self.interface_colour + str(value)
        canvas.create_text(5, size_of_board*20 + 20 + self.interface_height, text=text, fill='#000000', font=('Courier', 10), anchor='nw')




    def make_connections(self, path, localboard, is_for_real):
        #print(is_for_real)
        #for i in range(0, len(path)):
         #   path[i].printme()
        for i in range(0, len(path) - 1):
            path[i].dots_connected.append(path[i + 1])
            path[i + 1].dots_connected.append(path[i])
            
            
        path[len(path) - 1].dots_connected.append(path[0])
        path[0].dots_connected.append(path[len(path) - 1])
        
        if is_for_real == 'real bro':
            for i in range(0, len(path)):
                path[i].update()
        
        self.area = self.get_area(localboard)
        

        
        


    def find_connections(self, start, finish, localboard, is_for_real):    
        #depth first search
        #iterate through all possiple paths
        #choose one that goes from start to finish and is the longest
                                                                                                                                                                        #at this point i doubt that my code is the most efficient or readable
                                                                                                                                                                        #but my apologies, i tried my best
        #if start.ist_an_der_grenze() and finish.ist_an_der_grenze():
        conn_pretendents = []#for connection cases when borders are involved
            
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        matrix[start.x][start.y] = True
        matrix[finish.x][finish.y] = True
        connections = []

        def suchen(path):
            current = path[len(path) - 1]

            neighbours = current.get_accessible_neighbours(localboard)
                
                    
            for i in range(0, len(neighbours)):
                if neighbours[i].check_for_connection_with(current):
                    connections.append([neighbours[i], current])


                if neighbours[i].x == finish.x and neighbours[i].y == finish.y:
                    conn1 = False#conn1 and conn2 are just stupid variable names, the variables themselves 
                    conn2 = False#are used to check if connections contain (current and finish) pair

                    for j in range(0, len(connections)):
                        if connections[j][0].x == finish.x and connections[j][0].y == finish.y:
                            if connections[j][1].x == current.x and connections[j][1].y == current.y:
                                conn1 = True
                            
                        if connections[j][1].x == finish.x and connections[j][1].y == finish.y:
                            if connections[j][0].x == current.x and connections[j][0].y == current.y:
                                conn2 = True
                        
                    if conn1 == False and conn2 == False:
                        conn_pretendents.append(path)
                            
                    
                if matrix[neighbours[i].x][neighbours[i].y] == False:
                    matrix[neighbours[i].x][neighbours[i].y] = True
                    connections.append([current, neighbours[i]])

                    new_path = []
                    for j in range(0, len(path)):
                        new_path.append(path[j])
                    new_path.append(neighbours[i])

                    suchen(new_path)
            
        suchen([start])


        for i in range(0, len(conn_pretendents)):
            conn_pretendents[i].append(finish)

            
        maxlen = 0
        maxindex = -1
        for i in range(0, len(conn_pretendents)):
            if len(conn_pretendents[i]) > maxlen:
                maxindex = i
                maxlen = len(conn_pretendents[i])
        if len(conn_pretendents) > 0:
            self.make_connections(conn_pretendents[maxindex], localboard, is_for_real)


                            



        '''else:
            


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
                #print('path')
                #for i in range(0, len(path)):
                 #   path[i].printme()
                
                neighbours = current.get_accessible_neighbours(localboard)

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
                    
                    #print('processing')
                    #neighbours[i].printme()
                    #print(matrix[neighbours[i].x][neighbours[i].y])
                    if matrix[neighbours[i].x][neighbours[i].y] == False:
                        matrix[neighbours[i].x][neighbours[i].y] = True
                        
                        connections.append([current, neighbours[i]])

                        #here we cannot use the = operator, because it assigns arrays by reference
                        #but we need path to be isolated from new_path
                        new_path = []
                        for j in range(0, len(path)):
                            new_path.append(path[j])
                        new_path.append(neighbours[i])

                        keinenamenahnungen(new_path)
                    
        
            keinenamenahnungen([start])
        
            for i in range(0, len(connections_pretendents)):
                connections_pretendents[i].append(finish)
            
            #for i in range(0, len(connections)):
                #print('new')
                #connections[i][0].printme()
                #connections[i][1].printme()

            maxlen = 0
            maxindex = -1
            for i in range(0, len(connections_pretendents)):
                #print('new connection')
                #for j in range(0, len(connections_pretendents[i])):
                 #   connections_pretendents[i][j].printme()

                if len(connections_pretendents[i]) > maxlen:
                    maxindex = i
                    maxlen = len(connections_pretendents[i])
        
            self.make_connections(connections_pretendents[maxindex], localboard, is_for_real)'''


       



            



    def are_connections_possible(self, start, localboard, is_for_real):
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
                neighbours = front[i].get_accessible_neighbours(localboard)

                for j in range(0, len(neighbours)):
                    if matrix[neighbours[j].x][neighbours[j].y] == False:
                        vorbereitung.append(localboard[neighbours[j].x][neighbours[j].y])
                        matrix[neighbours[j].x][neighbours[j].y] = True

            front = vorbereitung
            wave.append(front)


        for i in range(0, len(wave)):
            for j in range(0, len(wave[i])):
                wave[i][j].connection_possibility(localboard, is_for_real)
                                    


            
                



    def put_dot(self):
        dot = Temporary_dot(-1, -1)
        response = '-'

        x = -1
        y = -1
        while response == '-' or check_for_position_acceptance(x, y, board) == False:
            print('player ' + self.interface_colour)
            print("write the coordinates where you want to place the dot")
            x = int(input('x: '))
            y = int(input('y: '))
            
    
            while check_for_position_acceptance(x, y, board) == False:
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
        self.are_connections_possible(board[x][y], board, 'real bro')
        time_spent = time.time() - time_spent
        global process_time
        print('time spent: %s' % time_spent)
        
        process_time += time_spent
        return 'ja ja arbeit arbeit'




    def choose_dot(self):
        start = time.time()

        preferred_one = self.get_the_best_place(board, 1, 1)
        preferredx = preferred_one[0]
        preferredy = preferred_one[1]
        print(str(preferredx) + ' ' + str(preferredy))
        board[preferredx][preferredy] = Dot(preferredx, preferredy, self, [])
        self.are_connections_possible(board[preferredx][preferredy], board, 'real bro')
        board[preferredx][preferredy].update()

        time_spent = time.time() - start
        global process_time
        process_time += time_spent
        print('time spent: %s' % time_spent)





    def get_the_best_place(self, board_to_work_with, max_iteration, current_iteration):
        #if current_iteration < max_iteration:
        
            maxneubereich = 0
            maxx = 0
            maxy = 0
            while check_for_position_acceptance(maxx, maxy, board_to_work_with) == False:
                if maxy < size_of_board - 1:
                    maxy += 1
                else:
                    maxy = 0
                    maxx += 1
            
            #check every possible iteration of given depth
            for x in range(0, size_of_board):
                for y in range(0, size_of_board):
                
                    localboard = []
                    for i in range(0, size_of_board):
                        row = []
                        for j in range(0, size_of_board):
                            dot_vorbereitung = Dot(0, 0, None, [])
                            dot_vorbereitung.x = board_to_work_with[i][j].x
                            dot_vorbereitung.y = board_to_work_with[i][j].y
                            dot_vorbereitung.team = board_to_work_with[i][j].team
                            for k in range(0, len(board_to_work_with[i][j].dots_connected)):
                                dot_vorbereitung.dots_connected.append(board_to_work_with[i][j].dots_connected[k])

                            row.append(dot_vorbereitung)
                        localboard.append(row)
                    

                    
                    
                    if check_for_position_acceptance(x, y, localboard) == True:
                        localboard[x][y].team = self
                        self.are_connections_possible(localboard[x][y], localboard, 'imaginary abstraction')
                        area = self.get_area(localboard)

                        if area > maxneubereich:
                            maxneubereich = area
                            maxx = x
                            maxy = y
                        
                        #me try make simple readable code
                        #me can not
                        #me write stupid code chunk
                        #my code be messy but worky
                        localboard[x][y].team = None
                        localboard[x][y].dots_connected = []

                        for i in range(0, size_of_board):
                            for j in range(0, size_of_board):
                                k = 0
                                while k < len(localboard[i][j].dots_connected):
                                    
                                    if localboard[i][j].dots_connected[k].x == x and localboard[i][j].dots_connected[k].y == y:
                                        del localboard[i][j].dots_connected[k]
                                    else:
                                        k += 1
                                    
                                    

                
                
            return [maxx, maxy]
    





global game_mode
response = ''
while response != 'with human' and response != 'with computer':
    print('select the game mode')
    print('if you want to play with another player, type "with human"')
    print('if you want to play with the computer, type "with computer"')
    response = input('')
    print('')
if response == 'with human':
    game_mode = 'twoplayer'
else:
    game_mode = 'bot'
    
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
os.system('cls')


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

for i in range(0, size_of_board):
    for j in range(0, size_of_board):    
        board[i][j].update()

players = [Player('#ff0000', 0, 'red', 0), Player('#00ff00', 0, 'green', 20), Player('#0000ff', 0, 'blue', 40), 
               Player('#bbbb00', 0, 'golden', 50),
               Player('#117733', 0, 'nocolouridea', 60), Player('#999999', 0, 'silver', 70)]

game_mode = 'bot'

if game_mode == 'twoplayer':
    number_of_players = 2

    n_players = []
    for i in range(0, number_of_players):
        n_players.append(players[i])
    players = n_players



    players[0].show_area()
    players[1].show_area()
    
    #board[0][0].team = players[0]
    #board[0][1].team = players[0]
    #board[1][2].team = players[0]
    #board[0][3].team = players[0]
    #players[0].are_connections_possible(board[1][2], board, 'real bro')

    is_procrastinating_with_homework = False
    while is_procrastinating_with_homework == False:
        for i in range(0, len(players)):
            operations += 1
            if players[i].put_dot() == 'schmetterling':
                is_procrastinating_with_homework = True
                break
            else:
                players[i].show_area()
                os.system('cls')
    print('Overall processor time: %s' % process_time)
    print('Average processor time per an operation: %s' % str(process_time/operations))

    if process_time/operations < 0.1:
        print('well done programmer, well done computer')



else:
    human = players[0]
    bot = players[1]

    human.show_area()
    bot.show_area()


    #board[0][0].team = bot
    #board[1][1].team = bot
    #board[1][2].team = bot
    #board[2][1].team = bot
    #board[1][3].team = bot
    #board[2][3].team = bot
    #board[0][1].team = bot
    #board[0][3].team = bot
    #board[0][4].team = bot


    #for i in range(0, size_of_board):
     #   for j in range(0, size_of_board):    
      #      board[i][j].update()

    #time.sleep(6)

    NV_is_waiting = False
    while NV_is_waiting == False:
        if human.put_dot() == 'schmetterling':
            NV_is_waiting = True
            break
        bot.choose_dot()
        operations += 2
    bot.choose_dot()
    print('Average processor time per one operation: %s' % str(process_time/operations))
    if process_time/operations < 2:
        print('well done coder, well done a clew of transistors')
