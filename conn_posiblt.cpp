#include <vector>
#include <iostream>
#include "classes.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

void suchen(std::vector<Dot> path, gboard & connections, matr & matrix, gboard & localboard)
{
    Dot current = path[path.size() - 1];
    int size = localboard.size();
    Dot self = path[0];
    std::vector<Dot> neighbours = current.get_accessible_neighbours(localboard);

    std::vector<Dot> cnnctns;
    bool besonderer_fall;
    std::vector<Dot> new_path;
    int free_neighbours;
    int dots_on_border;
    bool special_case;
    std::vector<Dot> special_case_neighbours;
    bool conn1;
    bool conn2;



    for (int i = 0; i < neighbours.size(); i++)
    {
        if (neighbours[i].is_connected_to(current))
        {
            cnnctns.clear();
            cnnctns.push_back(neighbours[i]);
            cnnctns.push_back(current);
            connections.push_back(cnnctns);
        }

        besonderer_fall = false;
        if (neighbours[i].ist_an_der_grenze(size))
        {
            if (self.ist_an_der_grenze(size))
            {
                if ((neighbours[i] == self) == false)
                {
                    besonderer_fall = true;
                }
            }
        }

        //if two ends are on different sides, then they automatically can be connected
        //if they are on one side, then we need to check if they are the only dots on side
        //from all the path
        if (besonderer_fall)
        {
            if (self.are_on_same_side(neighbours[i], size) == false)
            {
                //prevent the case when everything is already connected
                new_path.clear();
                new_path = path;
                new_path.push_back(neighbours[i]);

                free_neighbours = 0;
                for (int jj = 0; jj < new_path.size() - 1; jj++)
                {
                    if (new_path[jj].is_connected_to(new_path[jj + 1]) == false)
                    {
                        free_neighbours++;
                    }
                }
                if (free_neighbours > 0)
                {
                    std::cout << "found on different sides\n";
                    self.team.find_connections(self, neighbours[i], localboard);
                }
            }
            else
            {
                dots_on_border = 0;
                for (int j = 0; j < path.size(); j++)
                {
                    if (path[j].ist_an_der_grenze(size))
                    {
                        dots_on_border++;
                    }
                }
                if (dots_on_border > 2)
                {
                    //prevent the case when the beginning and the end of the chain are neighbours
                    special_case = false;
                    special_case_neighbours = self.get_accessible_neighbours(localboard);
                    for (int ii = 0; ii < special_case_neighbours.size(); ii++)
                    {
                        if (special_case_neighbours[ii] == neighbours[i])
                        {
                            special_case = true;
                        }
                    }

                    if (special_case == false)
                    {
                        new_path.clear();
                        new_path = path;
                        new_path.push_back(neighbours[i]);

                        free_neighbours = 0;
                        for (int jj = 0; jj < new_path.size() - 1; jj++)
                        {
                            if (new_path[jj].is_connected_to(new_path[jj + 1]) == false)
                            {
                                free_neighbours++;
                            }
                        }
                        if (free_neighbours > 0)
                        {
                            std::cout << "found on the same side\n";
                            self.team.find_connections(self, neighbours[i], localboard);
                        }
                    }
                }
            }
        }

        if (neighbours[i] == self)
        {
            conn1 = false;
            conn2 = false;
            for (int j = 0; j < connections.size(); j++)
            {
                if (connections[j][0] == self && connections[j][1] == current)
                {
                    conn1 = true;
                }
                if (connections[j][0] == current && connections[j][1] == self)
                {
                    conn2 = true;
                }
            }
            if (conn1 == false && conn2 == false)
            {
                cnnctns.clear();
                cnnctns.push_back(current);
                cnnctns.push_back(self);
                connections.push_back(cnnctns);
                std::cout << "found in the middle\n";
                self.team.find_connections(self, current, localboard);
            }
        }

        if (matrix[neighbours[i].x][neighbours[i].y] == false)
        {
            matrix[neighbours[i].x][neighbours[i].y] = true;

            cnnctns.clear();
            cnnctns.push_back(neighbours[i]);
            cnnctns.push_back(current);
            connections.push_back(cnnctns);

            new_path.clear();
            new_path = path;
            new_path.push_back(neighbours[i]);
            
            suchen(new_path, connections, matrix, localboard);
        }
    }
}

void Dot::connection_possibility(gboard & localboard)
{
    matr matrix;
    std::vector<bool> row;
    gboard connections;
    int size = localboard.size();

    for (int i = 0; i < size; i++)
    {
        row.clear();
        for (int j = 0; j < size; j++)
        {
            row.push_back(false);
        }
        matrix.push_back(row);
    }

    matrix[this->x][this->y] = true;

    std::vector<Dot> path;
    path.push_back(Dot(this->x, this->y, this->team, this->dots_connected));

    suchen(path, connections, matrix, localboard);
}