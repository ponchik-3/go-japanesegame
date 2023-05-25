#include <iostream>
#include <vector>
#include "classes.h"
#include "io_operators.h"

using std::cout;
using std::endl;
using std::cin;
using std::string;
using std::vector;

int main ()
{
    vector<vector<Dot>> board;
    const int size_of_board = 20;
    vector<Dot> row;

    for (int i = 0; i < size_of_board; i++)
    {
        row.clear();
        for (int j = 0; j < size_of_board; j++)
        {
            Player temp(0, "");
            Dot temporary(i, j);
            row.push_back(temporary);
        }
        board.push_back(row);
    }

    //cout << board << "\n\n\n";

    vector<Player> players;
    players.push_back(Player(0, "red"));
    players.push_back(Player(0, "green"));

    double process_time = 0.0;
    int operations = 0;

    //game loop
    bool is_procrastinating_with_homework = false;
    while (is_procrastinating_with_homework == false)
    {
        for (int i = 0; i < players.size(); i++)
        {
            operations++;
            if (players[i].putdot(board) == "Болгаром будеш")
            {
                is_procrastinating_with_homework = true;
                break;
            }
        }
    }
    return 0;
}
