#include <iostream>
using std::cout;
using std::cin;

void create_array(int array[], int array_size)
{
    for (int i = 0; i < array_size; i++)
    {
        array[i] = i;
    }
}

void output_array(int array[], int array_size)
{
    for (int i = 0; i < array_size; i++)
    {
        cout << array[i] << " ";
    }
    cout << std::endl;
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



int main()
{
    int arrau[10];
    int size = sizeof(arrau)/sizeof(int);
    
    create_array(arrau, size);

    output_array(arrau, size);

    leftshift(3, 8, arrau, size);

    output_array(arrau, size);
    return 0;
}