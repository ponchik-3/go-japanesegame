#include <vector>
#include "classes.h"

typedef std::vector<std::vector<Dot>> gboard;

std::vector<Dot> Dot::get_accessible_neighbours(gboard localboard)
{
    std::vector<Dot> neighbours;
    int x = this->x;
    int y = this->y;
    int size = localboard.size();

    if (x > 0 && y > 0)
    {
        if (localboard[x - 1][y - 1].team == this->team && localboard[x - 1][y].is_connected_to(localboard[x][y - 1]) == false)
        {
            neighbours.push_back(localboard[x - 1][y - 1]);
        }
    }

    if (y > 0)
    {
        if (localboard[x][y - 1].team == this->team)
        {
            neighbours.push_back(localboard[x][y - 1]);
        }
    }

    if (x < size - 1 && y > 0)
    {
        if (localboard[x + 1][y - 1].team == this->team && localboard[x][y - 1].is_connected_to(localboard[x + 1][y]) == false)
        {
            neighbours.push_back(localboard[x + 1][y - 1]);
        }
    }

    if (x < size - 1)
    {
        if (localboard[x + 1][y].team == this->team)
        {
            neighbours.push_back(localboard[x + 1][y]);
        }
    }

    if (x < size - 1 && y < size - 1)
    {
        if (localboard[x + 1][y + 1].team == this->team && localboard[x + 1][y].is_connected_to(localboard[x][y + 1]) == false)
        {
            neighbours.push_back(localboard[x + 1][y + 1]);
        }
    }

    if (y < size - 1)
    {
        if (localboard[x][y + 1].team == this->team)
        {
            neighbours.push_back(localboard[x][y + 1]);
        }
    }

    if (x > 0 && y < size - 1)
    {
        if (localboard[x - 1][y + 1].team == this->team && localboard[x][y + 1].is_connected_to(localboard[x - 1][y]) == false)
        {
            neighbours.push_back(localboard[x - 1][y + 1]);
        }
    }

    if (x > 0)
    {
        if (localboard[x - 1][y].team == this->team)
        {
            neighbours.push_back(localboard[x - 1][y]);
        }
    }

    return neighbours;
}