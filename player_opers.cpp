#include <string>
#include "classes.h"

bool Player::operator == (Player another)
{
    if (this->colour == another.colour)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool Player::operator != (Player another)
{
    if (this->colour == another.colour)
    {
        return false;
    }
    else
    {
        return true;
    }
}