#ifndef IO_OPERATORS
#define IO_OPERATORS

#include <iostream>
#include <vector>
#include "classes.h"
using std::cout;
using std::cin;
using std::ostream;
using std::istream;
using std::vector;

std::ostream& operator <<(std::ostream& out, Dot dot);

std::ostream& operator <<(std::ostream &out, Player player);

std::ostream& operator <<(std::ostream & out, vector<Dot> vect);

std::ostream& operator <<(std::ostream & out, vector<vector<Dot>> vect);

std::ostream & operator << (std::ostream & out, vector<vector<int>> vect);



#endif