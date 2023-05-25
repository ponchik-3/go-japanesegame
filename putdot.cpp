#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include "classes.h"

typedef std::vector<std::vector<Dot>> gboard;

/*bool isintegerinput(std::string input)
{
	std::vector<std::string> characters;
	//sorry for the kerbstone code, but it doesn't work otherwise
	characters.push_back("0");
	characters.push_back("1");
	characters.push_back("2");
	characters.push_back("3");
	characters.push_back("4");
	characters.push_back("5");
	characters.push_back("6");
	characters.push_back("7");
	characters.push_back("8");
	characters.push_back("9");


	bool is_in_character_list;
	for (int i = 0; i < input.length(); i++)
	{
		is_in_character_list = false;
		for (int j = 0; j < 10; j++)
		{
			if (characters[j] == input[i])
			{
				is_in_character_list = true;
			}
		}
		if (is_in_character_list == false)
		{
			return false;
		}
	}
	return true;
}*/

std::string Player::putdot(gboard &board)
{
	std::string response;
	int x;
	int y;
	response = "-";
	std::string xinput;
	std::string yinput;	

	while (response == "-" || check_for_position_acceptance(x, y, board) == false)
	{
		std::cout << "player " << this->colour << std::endl;
		std::cout << "write the coordinates where you want to place your dot\n";
		std::cout << "x: ";
		std::cin >> xinput;
		std::cout << "\n";

		/*if (isintegerinput(xinput) == false)
		{
			while (isintegerinput(xinput) == false)
			{
				if (xinput == "quit")
				{
					return "Болгаром будеш";
				}
				std::cout << "player " << this->colour << std::endl;
				std::cout << "be careful while typing and write the coordinates where you want to place your dot\n";
				std::cout << "x: ";
				std::cin >> xinput;
				std::cout << "\n";
			}
		}*/
		x = stoi(xinput);//as well as this function


		std::cout << "y: ";
		std::cin >> yinput;
		std::cout << "\n";

		/*if (isintegerinput(yinput) == false)
		{
			while (isintegerinput(yinput) == false)
			{
				if (yinput == "quit")
				{
					return "Болгаром будеш";
				}
				std::cout << "player " << this->colour << std::endl;
				std::cout << "be careful while typing and write the coordinates where you want to place your dot\n";
				std::cout << "y: ";
				std::cin >> yinput;
				std::cout << "\n";
			}
		}*/
		y = stoi(yinput);//as well as this function
		
		std::cout << check_for_position_acceptance(x, y, board) << std::endl;
		while (check_for_position_acceptance(x, y, board) == false)
		{
			std::cout << "enter value following rules\n";

			std::cout << "player " << this->colour << std::endl;
			std::cout << "write the coordinates where you want to place your dot\n";
			std::cout << "x: ";
			std::cin >> xinput;
			std::cout << "\n";

			/*if (isintegerinput(xinput) == false)
			{
				while (isintegerinput(xinput) == false)
				{
					if (xinput == "quit")
					{
						return "Болгаром будеш";
					}
					std::cout << "player " << this->colour << std::endl;
					std::cout << "be careful while typing and write the coordinates where you want to place your dot\n";
					std::cout << "x: ";
					std::cin >> xinput;
					std::cout << "\n";
				}
			}*/
			x = stoi(xinput);//as well as this function


			std::cout << "y: ";
			std::cin >> yinput;
			std::cout << "\n";

			/*if (isintegerinput(yinput) == false)
			{
				while (isintegerinput(yinput) == false)
				{
					if (yinput == "quit")
					{
						return "Болгаром будеш";
					}
					std::cout << "player " << this->colour << std::endl;
					std::cout << "be careful while typing and write the coordinates where you want to place your dot\n";
					std::cout << "y: ";
					std::cin >> yinput;
					std::cout << "\n";
				}
			}*/
			y = stoi(yinput);
		}

		std::cout << "validate your dot\n";
		std::cout << "if you are sure, type 'yes', else type '-'\n";
		std::cout << "if you want to wuit the game, type 'quit'\n";
		std::cin >> response;
		if (response == "quit")
		{
			return "Болгаром будеш";
		}
		while (response != "yes" && response != "-")
		{
			std::cout << "you have to press 'enter' or type '-'\n";
			std::cout << "if you are sure, type 'yes', else type '-'\n";
			std::cout << "if you want to wuit the game, type 'quit'\n";
			std::cin >> response;
		}
	}
	uint64_t begin = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
	
	board[x][y].team.colour = this->colour;
	board[x][y].team.area = this->area;
	this->are_connections_possible(board[x][y], board);
	uint64_t end = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
	std::cout << "time spent: " << end - begin << std::endl;
	return "ja ja arbeit arbeit";
}
