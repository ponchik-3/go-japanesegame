#include <vector>
#include "classes.h"
#include "io_operators.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

int Player::get_area(gboard localboard)
{
    int size = localboard.size();
    matr matrix;
    int area;
    int i;
    int j;
    std::vector<bool> row;
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

    i = 0;
    j = 0;
    area = 0;
    while (i < size && j < size)
    {
        temp.area = this->area;
        temp.colour = this->colour;
        if (matrix[i][j] == false && (localboard[i][j].team == temp) == false)
        {
            area = area + this->wave_for_area(matrix, i, j, localboard);
        }
        if (j == size - 1)
        {
            j = 0;
            i++;
        }
        else
        {
            j++;
        }
    }
    return area;
}