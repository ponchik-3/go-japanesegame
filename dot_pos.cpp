#include <vector>
#include "classes.h"

bool Dot::ist_an_der_grenze(int size)
{
    if (this->x == 0 || this->y == 0 || this->x == size - 1 || this->y == size - 1)
    {
        return true;
    }
    return false;
}

bool Dot::are_on_same_side(Dot fellow, int size)
{
    if (this->ist_an_der_grenze(size) && fellow.ist_an_der_grenze(size))
    {
        if (this->x == fellow.x && this->y == fellow.y)
        {
            return true;
        }
    }
    return false;
}