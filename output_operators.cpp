#include <iostream>
#include <vector>
#include "classes.h"
#include "io_operators.h"

using std::vector;
using std::endl;



std::ostream& operator << (std::ostream& out, Dot dot) 
{
    out << "x: " << dot.x << ";\t";
    out << "y: " << dot.y << ";\t";
    out << "team: " << dot.team.colour << ";\t";
    out << "dots connected length: " << dot.dots_connected.size() << ";\n";
    return out;
}

std::ostream& operator << (std::ostream &out, Player player)
{
    out << player.colour << endl << player.area << endl;
    return out;
}

std::ostream& operator <<(std::ostream & out, vector<Dot> vect)
{
    for (int i = 0; i < vect.size(); i++)
    {
        out << i << "\n" << vect[i] << endl;
    }
    return out;
}

std::ostream& operator <<(std::ostream & out, vector<vector<Dot>> vect)
{
    for (int i = 0; i < vect.size(); i++)
    {
        out << i << "\n" << vect[i] << endl;
    }
    return out;
}