#ifndef CLASSES_H
#define CLASSES_H

#include <iostream>
#include <vector>
#include <string>

class Dot;

typedef std::vector<std::vector<Dot>> gboard;
typedef std::vector<std::vector<bool>> matr;

bool check_for_position_acceptance(int x, int y, gboard localboard);

class Player
{
    public:
        int area;
        std::string colour;
        Player();
        Player(int area, std::string colour);
        
        bool operator == (Player another);

        bool operator != (Player another);

        std::string putdot(gboard & board);

        int wave_for_area(matr & array_matrix, int xcrdnt, int ycrdnt, gboard localboard);
        
        int get_area(gboard localboard);

        void make_connections(std::vector<Dot> path, gboard & localboard);

        void find_connections(Dot start, Dot finish, gboard & localboard);

        void are_connections_possible(Dot start, gboard & localboard);

        void choose_dot(gboard & board, int px, int py);

        void get_the_best_place(Player & opponent, int depth, gboard & board);
};

class Dot
{
    public:
        int x;
        int y;
        Player team;
        std::vector<Dot> dots_connected;
        Dot();
        Dot(int xc, int yc);
        Dot(int xcoordinate, int ycoordinate, Player _team, std::vector<Dot> _dots_connected);

        bool operator == (Dot fellow_dot);

        bool is_connected_to(Dot fellowdot);

        std::vector<Dot> get_accessible_neighbours(gboard localboard);

        bool ist_an_der_grenze(int size);

        bool are_on_same_side(Dot fellowdot, int size);

        void connection_possibility(gboard & localboard);
};



#endif