#include <iostream>
#include <vector>
#include "classes.h"
#include "io_operators.h"

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

void Player::choose_dot(gboard & board, int px, int py)
{   
    board[px][py].team.colour = this->colour;
	Player temp(this->area, this->colour);
    temp.are_connections_possible(board[px][py], board);
	std::cout << "Chosen dot: " << board[px][py] << std::endl;

    for (int i = 0; i < board.size(); i++)
	{
		for (int j = 0; j < board.size(); j++)
		{
			if (board[j][i].team.colour == "")
			{
				std::cout << "' ";
			}
			else
			{
				std::cout << board[j][i].team.colour << " ";
			}
		}
		std::cout << std::endl;
	}
}