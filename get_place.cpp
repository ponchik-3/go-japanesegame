#include <iostream>
#include <vector>
#include <chrono>
#include "classes.h"
#include "io_operators.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

struct Utility_of_dot
{
    int x;
    int y;
    int utility;
    Utility_of_dot(){}
    Utility_of_dot(int _x, int _y, int _utility)
    {
        this->x = _x;
        this->y = _y;
        this->utility = _utility;
    }
};

void clear_dot(int x, int y, gboard & localboard)
{
    int size = localboard.size();
    int x_begin = 0;
    int x_end = 0;
    int y_begin = 0;
    int y_end = 0;

    if (x == 0)
    {
        x_begin = 0;
        x_end = 1;
    }
    else
    {
        if (x == size - 1)
        {
            x_begin = size - 2;
            x_end = size - 1;
        }
        else
        {
            x_begin = x - 1;
            x_end = x + 1;
        }
    }

    if (y == 0)
    {
        y_begin = 0;
        y_end = 1;
    }
    else
    {
        if (y == size - 1)
        {
            y_begin = size - 2;
            y_end = size - 1;
        }
        else
        {
            y_begin = x - 1;
            y_end = x + 1;
        }
    }

    int k;
    for (int i = x_begin; i < x_end - 1; i++)
    {
        for (int j = y_begin; j < y_end - 1; j++)
        {
            k = 0;
            while (k < localboard[i][j].dots_connected.size())
            {
                if (localboard[i][j].dots_connected[k] == localboard[x][y])
                {
                    localboard[i][j].dots_connected.erase(localboard[i][j].dots_connected.begin() + k);
                }
                else
                {
                    k++;
                }
            }
        }
    }
}


int iterations(gboard board_to_work_with, Player & opponent, int max_iteration,
                int current_iteration, std::vector<Utility_of_dot> & utilities, Player self)
{
    //imitate the moves of both human and computer
    //until current_iteration reaches max_iteration
    int size = board_to_work_with.size();
    gboard localboard;
    int maxneubereich;
    int maxx;
    int maxy;
    int area;

    if (current_iteration < max_iteration)
    {
        int x = 0;
        int y = 0;
        while (x < size && y < size)
        {
            localboard = board_to_work_with;

            if (check_for_position_acceptance(x, y, localboard))
            {
                localboard[x][y].team.colour = self.colour;
                self.are_connections_possible(localboard[x][y], localboard);
                
                int xx = 0;
                int yy = 0;
                while (xx < size && yy < size)
                {
                    if (check_for_position_acceptance(xx, yy, localboard))
                    {
                        localboard[xx][yy].team.colour = opponent.colour;
                        opponent.are_connections_possible(localboard[xx][yy], localboard);

                        iterations(localboard, opponent, max_iteration, current_iteration + 1, utilities, self);
                        localboard[xx][yy].team.colour = "";
                        clear_dot(xx, yy, localboard);
                    }

                    if (yy < size - 1)
                    {
                        yy++;
                    }
                    else
                    {
                        yy = 0;
                        xx++;
                    }
                }
            }

            if (y < size - 1)
            {
                y++;
            }
            else
            {
                y = 0;
                x++;
            }
        }
    }

    else
    {
        if (current_iteration == max_iteration)
        {
            maxneubereich = opponent.get_area(board_to_work_with);
            maxx = 0;
            maxy = 0;
            while (check_for_position_acceptance(maxx, maxy, board_to_work_with) == false)
            {
                if (maxy < size - 1)
                {
                    maxy++;
                }
                else
                {
                    maxy = 0;
                    maxx++;
                    if (maxx > size - 1)
                    {
                        return 0;
                    }
                }
            }
            std::cout << "maxcoords  " << maxx << " " << maxy << "\n";

            //check every possible iteration
            int x = maxx;
            int y = maxy;
            while (x < size && y < size)
            {
                localboard = board_to_work_with;

                if (check_for_position_acceptance(x, y, localboard))
                {
                    localboard[x][y].team.colour = self.colour;
                    self.are_connections_possible(localboard[x][y], localboard);
                    area = self.get_area(localboard) - opponent.get_area(localboard);

                    if (area > maxneubereich)
                    {
                        maxneubereich = area;
                        maxx = x;
                        maxy = y;
                    }
                }
                if (y < size - 1)
                {
                    y++;
                }
                else
                {
                    y = 0;
                    x++;
                }
            }

            Utility_of_dot temp(maxx, maxy, maxneubereich);
            utilities.push_back(temp);
        }
    }
    return 0;
}

void Player::get_the_best_place(Player & opponent, int depth, gboard & board)
{
    int size = board.size();
    std::vector<Utility_of_dot> utilities;
    Player temp(this->area, this->colour);

    uint64_t start = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();

    iterations(board, opponent, depth, 1, utilities, temp);
    
    Utility_of_dot maxutility;
    
    maxutility.x = utilities[0].x;
    maxutility.y = utilities[0].y;
    maxutility.utility = utilities[0].utility;
    
    int maxutilityindex = 0;
    for (int i = 1; i < utilities.size(); i++)
    {
        if (maxutility.utility < utilities[i].utility)
        {
            maxutility = utilities[i];
            maxutilityindex = i;
        }
    }
    std::cout << "checktest " << maxutility.x << " " << maxutility.y << "\n";

    uint64_t finish = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();

    std::cout << utilities[maxutilityindex].x << " " << utilities[maxutilityindex].y << std::endl;

    std::cout << "\n\nboard\n" << board;

    std::cout << "Time spent: " << (finish - start)/1000.0 << "\n";
    this->choose_dot(board, maxutility.x, maxutility.y);
}