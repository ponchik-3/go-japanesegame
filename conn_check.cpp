#include <vector>
#include "classes.h"

bool Dot::is_connected_to(Dot fellowdot)
{
	if (this->team == fellowdot.team)
	{
		for (int i = 0; i < this->dots_connected.size(); i++)
		{
			if (this->dots_connected[i] == fellowdot)
			{
				return true;
			}
		}
	}
	return false;
}
