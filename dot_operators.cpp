#include "classes.h"


bool Dot::operator == (Dot fellow_dot)
{
    if (this->x == fellow_dot.x && this->y == fellow_dot.y)
    {
        return true;
    }
    else
    {
        return false;
    }
}