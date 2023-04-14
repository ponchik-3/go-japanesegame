#include <iostream>
#include <cmath>
#include <cstdlib>//for generating random numbers

void create_array(int array[], int array_size)
{
    srand((unsigned) time(NULL));
    for (int i = 0; i < array_size; i++)
    {
        array[i] = rand() % 10;
    }
}

void output_array(int array[], int array_size)
{
    for (int i = 0; i < array_size; i++)
    {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}



void leftshift(int start, int finish, int arr[], int array_size)
{
    int bank = arr[start];
    for(int i = start; i < finish; i++)
    {
        arr[i] = arr[i + 1];
    }
    arr[finish] = bank;
}


void rightshift(int start, int finish, int arr[], int array_size)
{
    int bank = arr[finish];
    for(int i = finish; i > start; i--)
    {
        arr[i] = arr[i - 1];
    }
    arr[start] = bank;
}



int quicksort(int start, int finish, int array[], int size)
{
    if (start < finish) 
    {
        //calculate middle
        int middle = floor((finish - start)/2.0) + start;
        
        //sort left half
        int i = start;
        while(i < middle) 
        {
            if(array[i] < array[middle])
            {
                i++;
            }
            else
            {
                leftshift(i, middle, array, size);
                middle--;
            }
        }

        //sort right half
        i = finish;
        while(i > middle) 
        {
            if(array[i] > array[middle])
            {
                i--;
            }
            else
            {
                rightshift(middle, i, array, size);
                middle++;
            }
        }

        quicksort(start, middle - 1, array, size);
        quicksort(middle + 1, finish, array, size);
        return 0;
    }
    else
    {
        return 0;
    }
}



int main()
{
    const int x = 10;
    int array[x];
    create_array(array, x);
    output_array(array, x);
    quicksort(0, x - 1, array, x);
    std::cout << "sorted\n";
    output_array(array, x);

    return 0;
}