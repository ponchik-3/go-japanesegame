#include <vector>
#include "classes.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

void Player::are_connections_possible(Dot start, gboard & localboard)
{
    matr matrix;
    gboard wave;
    int size = localboard.size();
    std::vector<bool> row;
    std::vector<Dot> front;
    std::vector<Dot> vorbereitung;
    std::vector<Dot> neighbours;

    for (int i = 0; i < size; i++)
    {
        row.clear();
        for (int j = 0; j < size; j++)
        {
            row.push_back(false);
        }
        matrix.push_back(row);
    }

    front.push_back(start);
    wave.push_back(front);
    matrix[start.x][start.y] = true;

    while (front.size() > 0)
    {
        vorbereitung.clear();

        for (int i = 0; i < front.size(); i++)
        {
            neighbours = front[i].get_accessible_neighbours(localboard);

            for (int j = 0; j < neighbours.size(); j++)
            {
                if (matrix[neighbours[j].x][neighbours[j].y] == false)
                {
                    vorbereitung.push_back(localboard[neighbours[j].x][neighbours[j].y]);
                    matrix[neighbours[j].x][neighbours[j].y] = true;
                }
            }
        }

        front = vorbereitung;
        wave.push_back(front);
    }
    for (int i = 0; i < wave.size(); i++)
    {
        for (int j = 0; j < wave[i].size(); j++)
        {
            wave[i][j].connection_possibility(localboard);
        }
    }
}