#include <vector>
#include "classes.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

int Player::wave_for_area(matr & array_matrix, int xcrdnt, int ycrdnt, gboard localboard)
{
    int size = localboard.size();
    matr matrix;
    gboard wave;
    std::vector<Dot> front;
    std::vector<bool> row;
    int sides;
    int area;
    std::vector<Dot> vorbereitung;
    Player temp;

    for (int i = 0; i < size; i++)
    {
        row.clear();
        for (int j = 0; j < size; j++)
        {
            row.push_back(false);
        }
        matrix.push_back(row);
    }
    matrix[xcrdnt][ycrdnt] = true;
    front.push_back(localboard[xcrdnt][ycrdnt]);
    wave.push_back(front);

    while (front.size() > 0)
    {
        vorbereitung.clear();
        for (int i = 0; i < front.size(); i++)
        {
            int x = front[i].x;
            int y = front[i].y;
            
            temp.area = this->area;
            temp.colour = this->colour;

            if (x > 0 && y > 0)
            {
                if ((localboard[x - 1][y].team == temp) == false && localboard[x - 1][y].is_connected_to(localboard[x][y - 1]) == false)
                {
                    if (matrix[x - 1][y - 1] == false && localboard[x - 1][y - 1].team != temp)
                    {
                        vorbereitung.push_back(localboard[x - 1][y - 1]);
                        matrix[x - 1][y - 1] = true;
                    }
                }
            }

            if (y > 0)
            {
                if (localboard[x][y - 1].team != temp && matrix[x][y - 1] == false)
                {
                    vorbereitung.push_back(localboard[x][y - 1]);
                    matrix[x][y - 1] = true;
                }
            }
            
            if (x < size - 1 && y > 0)
            {
                if ((localboard[x][y - 1].team == temp) == false && localboard[x][y - 1].is_connected_to(localboard[x + 1][y]) == false)
                {
                    if (matrix[x + 1][y - 1] == false && localboard[x + 1][y - 1].team != temp)
                    {
                        vorbereitung.push_back(localboard[x + 1][y - 1]);
                        matrix[x + 1][y - 1] = true;
                    }
                }
            }
            
            if (x < size - 1)
            {
                if (localboard[x + 1][y].team != temp && matrix[x + 1][y] == false)
                {
                    vorbereitung.push_back(localboard[x + 1][y]);
                    matrix[x + 1][y] = true;
                }
            }
            
            if (x < size - 1 && y < size - 1)
            {
                if ((localboard[x + 1][y].team == temp) == false && localboard[x + 1][y].is_connected_to(localboard[x][y + 1]) == false)
                {
                    if (matrix[x + 1][y + 1] == false && localboard[x + 1][y + 1].team != temp)
                    {
                        vorbereitung.push_back(localboard[x + 1][y + 1]);
                        matrix[x + 1][y + 1] = true;
                    }
                }
            }
            
            if (y < size - 1)
            {
                if (localboard[x][y + 1].team != temp && matrix[x][y + 1] == false)
                {
                    vorbereitung.push_back(localboard[x][y + 1]);
                    matrix[x][y + 1] = true;
                }
            }
            
            if (x > 0 && y < size - 1)
            {
                if ((localboard[x][y + 1].team == temp) == false && localboard[x][y + 1].is_connected_to(localboard[x - 1][y]) == false)
                {
                    if (matrix[x - 1][y + 1] == false && localboard[x - 1][y + 1].team != temp)
                    {
                        vorbereitung.push_back(localboard[x - 1][y + 1]);
                        matrix[x - 1][y + 1] = true;
                    }
                }
            }

            if (x > 0)
            {
                if (localboard[x - 1][y].team != temp && matrix[x - 1][y] == false)
                {
                    vorbereitung.push_back(localboard[x - 1][y]);
                    matrix[x - 1][y] = true;
                }
            }
        }
        front = vorbereitung;
        wave.push_back(front);
    }

    sides = 0;
    for (int i = 0; i < wave.size(); i++)
    {
        for (int j = 0; j < wave[i].size(); j++)
        {
            if (wave[i][j].ist_an_der_grenze(size))
            {
                sides++;
            }
        }
    }
    area =  0;
    for (int i = 0; i < wave.size(); i++)
    {
        for (int j = 0; j < wave[i].size(); j++)
        {
            array_matrix[wave[i][j].x][wave[i][j].y] = true;
        }
    }
    if (sides < size*2)
    {
        for (int i = 0; i < wave.size(); i++)
        {
            area = area + wave[i].size();
        }
    }
    return area;
}