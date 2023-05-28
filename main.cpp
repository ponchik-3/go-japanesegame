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

    string response;
    cout << "If you want to play with human, type 'human'\nIf you want to play with computer, type 'computer'\n";
    cin >> response;

    while ((response == "human") == false && (response == "computer") == false)
    {
        cout << "Type carefully\n";
        cout << "If you want to play with human, type 'with human'\nIf you want to play with computer, type 'with computer'\n";
        cin >> response;
    }
    

    if (response == "human")
    {
        vector<Player> players;
        players.push_back(Player(0, "#"));
        players.push_back(Player(0, "@"));

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

        std::cout << "Area circled by Player " << players[0].colour << ": " << players[0].area << std::endl;
        std::cout << "Area circled by Player " << players[1].colour << ": " << players[1].area << std::endl;
        if (players[0].area > players[1].area)
        {
            std::cout << "Player " << players[0].colour << " won!\n";
        }
        else
        {
            if (players[0].area < players[1].area)
            {
                std::cout << "Player " << players[1].colour << " won!\n";
            }
            else
            {
                std::cout << "p8q274qkgerli\n";
            }
        }
    }
    /*else
    {
        Player human(0, "H");
        Player bot(0, "B");

        double process_time = 0.0;
        int operations = 0;

        bool NV_is_waiting = false;
        while (NV_is_waiting == false)
        {
            operations++;
            if (human.putdot(board) == "Болгаром будеш")
            {
                NV_is_waiting = true;
                break;
            }
            bot.get_the_best_place(human, 1, board);
            operations++;
        }
    }*/

    return 0;
}
