#include <vector>
#include <iostream>
#include "classes.h"
#include "io_operators.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

void suchen(std::vector<Dot> path, matr & matrix, gboard & localboard, gboard & connections, 
            gboard & conn_pretendents, Dot finish)
{
    Dot current = path[path.size() - 1];
    std::vector<Dot> neighbours = current.get_accessible_neighbours(localboard);
    std::vector<Dot> cnctns;
    std::vector<Dot> new_path;
    bool conn1;
    bool conn2;

    for (int i = 0; i < neighbours.size(); i++)
    {
        if (neighbours[i].is_connected_to(current))
        {
            cnctns.clear();
            cnctns.push_back(neighbours[i]);
            cnctns.push_back(current);
            connections.push_back(cnctns);
        }
        if (neighbours[i] == finish)
        {
            conn1 = false;//conn1 and conn2 are just stupid variable names, the variables themselves 
            conn2 = false;//are used to check if connections contain (current and finish) pair
            for (int j = 0; j < connections.size(); j++)
            {
                if (connections[j][0] == finish && connections[j][1] == current)
                {
                    conn1 = true;
                }
                if (connections[j][0] == current && connections[j][1] == finish)
                {
                    conn2 = true;
                }

                if (conn1 == false && conn2 == false)
                {
                    conn_pretendents.push_back(path);
                }
            }
        }
        if (matrix[neighbours[i].x][neighbours[i].y] == false)
        {
            matrix[neighbours[i].x][neighbours[i].y] = true;
            cnctns.clear();
            cnctns.push_back(neighbours[i]);
            cnctns.push_back(current);
            connections.push_back(cnctns);

            new_path.clear();
            new_path = path;
            new_path.push_back(neighbours[i]);

            suchen(new_path, matrix, localboard, connections, conn_pretendents, finish);
        }
    }
}

void Player::find_connections(Dot start, Dot finish, gboard & localboard)
{
    //depth first search
    //iterate through all possiple paths
    //choose one that goes from start to finish and is the longest
    int size = localboard.size();
    gboard conn_pretendents;
    matr matrix;
    gboard connections;
    std::vector<bool> row;

    for (int i = 0; i < size; i++)
    {
        row.clear();
        for (int j = 0; j < size; j++)
        {
            row.push_back(false);
        }
        matrix.push_back(row);
    }

    matrix[start.x][start.y] = true;
    matrix[finish.x][finish.y] = true;
    std::vector<Dot> starter;
    starter.push_back(start);

    suchen(starter, matrix, localboard, connections, conn_pretendents, finish);

    for (int i = 0; i < conn_pretendents.size(); i++)
    {
        conn_pretendents[i].push_back(finish);
    }
    int maxsize = 0;
    int maxindex = -1;
    for (int i = 0; i < conn_pretendents.size(); i++)
    {
        if (conn_pretendents[i].size() > maxsize)
        {
            maxindex = i;
            maxsize = conn_pretendents[i].size();
        }
    }
    if (conn_pretendents.size() > 0)
    {
        std::cout << conn_pretendents[maxindex] << std::endl;
        this->make_connections(conn_pretendents[maxindex], localboard);
    }
}