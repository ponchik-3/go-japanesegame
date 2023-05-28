#include <vector>
#include "classes.h"

void Player::make_connections(std::vector<Dot> path, gboard & localboard)
{
    for (int i = 0; i < path.size() - 1; i++)
    {
        localboard[path[i].x][path[i].y].dots_connected.push_back(localboard[path[i + 1].x][path[i + 1].y]);
        localboard[path[i + 1].x][path[i + 1].y].dots_connected.push_back(localboard[path[i].x][path[i].y]);
    }
    localboard[path[path.size() - 1].x][path[path.size() - 1].y].dots_connected.push_back(localboard[path[0].x][path[0].y]);
    localboard[path[0].x][path[0].y].dots_connected.push_back(localboard[path[path.size() - 1].x][path[path.size() - 1].y]);

    this->area = this->get_area(localboard);
    std::cout << "area: " << this->area << "\n\n";
}