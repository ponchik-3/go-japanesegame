#include <iostream>
#include <vector>
#include <string>
#include "classes.h"

Player::Player(){}

Player::Player(int _area, std::string _colour)
{
    this->area = _area;
    this->colour = _colour;
}

Dot::Dot(){}

Dot::Dot(int xc, int yc)
{
    this->x = xc;
    this->y = yc;
    std::vector<Dot> empty;
    Player empty_p(0, "");
    this->dots_connected = empty;
    this->team = empty_p;
}

Dot::Dot(int xcoordinate, int ycoordinate, Player _team, std::vector<Dot> _dots_connected)
{
    this->x = xcoordinate;
    this->y = ycoordinate;
    this->team = _team;
    this->dots_connected = _dots_connected;
}

