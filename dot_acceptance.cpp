#include <vector>
#include <iostream>
#include "classes.h"
typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

bool check_for_position_acceptance(int x, int y, gboard localboard)
{
    int size = localboard.size();

    if (x < 0 || x > size - 1 || y < 0 || y > size - 1)
    {
        return false;
    }
    if (localboard[x][y].team.colour != "")
    {
        return false;
    }

    //wave walkthrough
    //for english audience - breadth first search
    //will determine if the placement is acceptable by counting accessible side knots
    int sides = 0;

    matr matrix;
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
    

    std::vector<Dot> front;
    front.push_back(localboard[x][y]);

    int cx;
    int cy;
    std::vector<Dot> nextfront;
    
    while (front.size() > 0)
    {
        nextfront.clear();
        for (int i = 0; i < front.size(); i++)
        {
            cx = front[i].x;
            cy = front[i].y;
            
            if (cy > 0)
            {
                if (localboard[cx][cy - 1].team.colour == "" && matrix[cx][cy - 1] == false)
                {
                    nextfront.push_back(localboard[cx][cy - 1]);
                    matrix[cx][cy - 1] = true;
                }
            }

            if (cx < size - 1)
            {
                if (localboard[cx + 1][cy].team.colour == "" && matrix[cx + 1][cy] == false)
                {
                    nextfront.push_back(localboard[cx + 1][cy]);
                    matrix[cx + 1][cy] = true;
                }
            }

            if (cy < size - 1)
            {
                if (localboard[cx][cy + 1].team.colour == "" && matrix[cx][cy + 1] == false)
                {
                    nextfront.push_back(localboard[cx][cy + 1]);
                    matrix[cx][cy + 1] = true;
                }
            }

            if (cx > 0)
            {
                if (localboard[cx - 1][cy].team.colour == "" && matrix[cx - 1][cy] == false)
                {
                    nextfront.push_back(localboard[cx - 1][cy]);
                    matrix[cx - 1][cy] = true;
                }
            }



            if (cx > 0 && cy > 0)
            {
                if (localboard[cx - 1][cy - 1].team.colour == "" && matrix[cx - 1][cy - 1] == false
                    && localboard[cx - 1][cy].is_connected_to(localboard[cx][cy - 1]) == false)
                {
                    nextfront.push_back(localboard[cx - 1][cy - 1]);
                    matrix[cx - 1][cy - 1] = true;
                }
            }

            if (cx < size - 1 && cy > 0)
            {
                if (localboard[cx + 1][cy - 1].team.colour == "" && matrix[cx + 1][cy - 1] == false
                    && localboard[cx][cy - 1].is_connected_to(localboard[cx + 1][cy]) == false)
                {
                    nextfront.push_back(localboard[cx + 1][cy - 1]);
                    matrix[cx + 1][cy - 1] = true;
                }
            }

            if (cx < size - 1 && cy < size - 1)
            {
                if (localboard[cx + 1][cy + 1].team.colour == "" && matrix[cx + 1][cy + 1] == false
                    && localboard[cx + 1][cy].is_connected_to(localboard[cx][cy + 1]) == false)
                {
                    nextfront.push_back(localboard[cx + 1][cy + 1]);
                    matrix[cx + 1][cy + 1] = true;
                }
            }

            if (cx > 0 && cy < size - 1)
            {
                if (localboard[cx - 1][cy + 1].team.colour == "" && matrix[cx - 1][cy + 1] == false
                    && localboard[cx][cy + 1].is_connected_to(localboard[cx - 1][cy]) == false)
                {
                    nextfront.push_back(localboard[cx - 1][cy + 1]);
                    matrix[cx - 1][cy + 1] = true;
                }
            }
        }
        
        front.clear();
        for (int i = 0; i < nextfront.size(); i++)
        {
            front.push_back(nextfront[i]);
        }
    }
    
    //count the sides
    for (int i = 0; i < size; i++)
    {
        
        if (matrix[0][i] == true)
        {
            sides++;
        }
        if (matrix[i][0] == true)
        {
            sides++;
        }
        if (matrix[size - 1][i] == true)
        {
            sides++;
        }
        if (matrix[i][size - 1] == true)
        {
            sides++;
        }
    }
    

    if (sides > size*2)
    {
        return true;
    }
    else
    {
        return false;
    }
}