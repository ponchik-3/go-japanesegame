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
        print(sides)
        
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
    def __init__(self, colour, area):
        self.colour = colour
        self.area = area

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
        #wave walkthrough
        #save all fronts
        #find path from start to finish
        start.printme()
        finish.printme()
        matrix = []
        for i in range(0, size_of_board):
            row = []
            for j in range(0, size_of_board):
                row.append(False)
            matrix.append(row)
        
        wave = [[start]]#array of fronts
        matrix[start.x][start.y] = True
        front = []
        
        #finish cannot be in the first front
                                                                                                                                                                        #at this point, i doubt that my code is the most organized or readable or effecient
                                                                                                                                                                        #but i don't care
        for j in range(0, len(start.dots_connected)):
            if matrix[start.dots_connected[j].x][start.dots_connected[j].y] == False:
                if start.dots_connected[j].x != start.x and start.dots_connected[j].y != start.y:
                    front.append(start.dots_connected[j])
                    matrix[start.dots_connected[j].x][start.dots_connected[j].y] = True


        if start.x > 0 and start.y > 0 and (start.x - 1 != finish.x or start.y - 1 != finish.y):
            if matrix[start.x - 1][start.y - 1] == False and board[start.x - 1][start.y - 1].team == self:        #*
                if board[start.x][start.y - 1].check_for_connection_with(board[start.x - 1][start.y]) == False:   # @
                    front.append(board[start.x - 1][start.y - 1])                                                 #
                    matrix[start.x - 1][start.y - 1] = True

        if start.y > 0 and (start.x != finish.x or start.y - 1 != finish.y):
            if matrix[start.x][start.y - 1] == False and board[start.x][start.y - 1].team == self:# *
                front.append(board[start.x][start.y - 1])                                         # @
                matrix[start.x][start.y - 1] = True                                               #

        if start.x < size_of_board - 1 and start.y > 0 and (start.x + 1 != finish.x or start.y - 1 != finish.y):
            if matrix[start.x + 1][start.y - 1] == False and board[start.x + 1][start.y - 1].team == self:         #  *
                if board[start.x][start.y - 1].check_for_connection_with(board[start.x + 1][start.y]) == False:    # @
                    front.append(board[start.x + 1][start.y - 1])                                                  #
                    matrix[start.x + 1][start.y - 1] = True

        if start.x < size_of_board - 1 and (start.x + 1 != finish.x or start.y != finish.y):
            if matrix[start.x + 1][start.y] == False and board[start.x + 1][start.y].team == self:#
                front.append(board[start.x + 1][start.y])                                         # @*
                matrix[start.x + 1][start.y] = True                                               #
            
        if start.x < size_of_board - 1 and start.y < size_of_board - 1 and (start.x + 1 != finish.x or start.y + 1 != finish.y):
            if matrix[start.x + 1][start.y + 1] == False and board[start.x + 1][start.y + 1].team == self:         #
                if board[start.x][start.y + 1].check_for_connection_with(board[start.x + 1][start.y]) == False:    # @
                    front.append(board[start.x + 1][start.y + 1])                                                  #  *
                    matrix[start.x + 1][start.y + 1] = True

        if start.y < size_of_board - 1 and (start.x != finish.x or start.y + 1 != finish.y):
            if matrix[start.x][start.y + 1] == False and board[start.x][start.y + 1].team == self:#
                front.append(board[start.x][start.y + 1])                                         # @
                matrix[start.x][start.y + 1] = True                                               # *

        if start.x > 0 and start.y < size_of_board - 1 and (start.x - 1 != finish.x or start.y + 1 != finish.y):
            if matrix[start.x - 1][start.y + 1] == False and board[start.x - 1][start.y + 1].team == self:         #
                if board[start.x][start.y + 1].check_for_connection_with(board[start.x - 1][start.y]) == False:    # @
                    front.append(board[start.x - 1][start.y + 1])                                                  #*
                    matrix[start.x - 1][start.y + 1] = True

        if start.x > 0 and (start.x - 1 != finish.x or start.y != finish.y):
            if matrix[start.x - 1][start.y] == False and board[start.x - 1][start.y].team == self:#
                front.append(board[start.x - 1][start.y])                                         #*@
                matrix[start.x - 1][start.y] = True                                               #
            

        wave.append(front)


        while len(front) > 0:
            vorbereitung = []

            for i in range(0, len(front)):
                for j in range(0, len(front[i].dots_connected)):
                    if matrix[front[i].dots_connected[j].x][front[i].dots_connected[j].y] == False:
                        vorbereitung.append(front[i].dots_connected[j])
                        matrix[front[i].dots_connected[j].x][front[i].dots_connected[j].y] = True


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
            front = vorbereitung
            wave.append(front)

        for i in range(0, len(wave)):
            for j in range(0, len(wave[i])):
                wave[i][j].printme()

        #print(len(wave))
        path = []
        def link(path):
            if len(path) < len(wave) - 1:
                #print(str(len(wave[len(path)])) + ' ' + str(len(path)))
                for i in range(0, len(wave[len(path)])):
                    if abs(wave[len(path)][i].x - path[len(path) - 1].x) < 2 and abs(wave[len(path)][i].y - path[len(path) - 1].y) < 2:
                        new_path = path
                        new_path.append(wave[len(path)][i])
                        link(new_path)
            else:
                self.make_connections(path)
                return
        path.append(start)
        link(path)



            



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
        while len(front) > 0:
            vorbereitung = []

            for i in range(0, len(front)):
                for j in range(0, len(front[i].dots_connected)):
                    if matrix[front[i].dots_connected[j].x][front[i].dots_connected[j].y] == False:
                        vorbereitung.append(front[i].dots_connected[j])
                        matrix[front[i].dots_connected[j].x][front[i].dots_connected[j].y] = True


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
                            #print('found')
                            self.find_connections(vorbereitung[i], vorbereitung[j])
                            return
                for j in range(0, len(front)):
                    for k in range(0, len(front)):
                        if j != k:
                            if abs(vorbereitung[i].x - front[j].x) < 2 and abs(vorbereitung[i].y - front[j].y) < 2:
                                if abs(vorbereitung[i].x - front[k].x) < 2 and abs(vorbereitung[i].y - front[k].y) < 2:
                                    #print('found in other way')
                                    self.find_connections(vorbereitung[i], front[k])
                                    return 
                                    
                        
            
            front = vorbereitung


            
                



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
        row.append(dot)

    board.append(row)



#board[0][0].team = players[0]
#board[1][0].team = players[0]
#board[2][1].team = players[0]
#board[2][2].team = players[0]
#board[1][3].team = players[0]
#board[1][2].team = players[0]
#board[0][1].team = players[0]
#board[1][1].team = players[0]


for i in range(0, size_of_board):
    for j in range(0, size_of_board):    
        board[i][j].update()


#players[0].are_connections_possible(board[1][0])


#players[1].put_dot()
#time.sleep(5)
is_procrastinating_with_homework = False
while is_procrastinating_with_homework == False:
    for i in range(0, len(players)):
        if players[i].put_dot() == 'schmetterling':
            is_procrastinating_with_homework = True
            break
