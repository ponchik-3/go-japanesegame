#include <iostream>

int main()
{
    int arr[5];
    for (int i = 0; i < sizeof(arr)/sizeof(int); i++)
    {
        arr[i] = i + 1;
    }
    
    //write array
    for (int i = 0; i < sizeof(arr)/sizeof(int); i++)
    {
        std::cout << arr[i] << " ";
    }
    
    int length = sizeof(arr)/sizeof(int);
    
    //std::cout << length;
    void write() 
    {
        std::cout << 
    }
    
    
    //shift array
    int storage = arr[0];
    for (int i = 0; i < length - 1; i++) 
    {
      arr[i] = arr[i + 1];
    }
    arr[length - 1] = storage;
    
    
    
    std::cout << "\n";
    
    for (int i = 0; i < sizeof(arr)/sizeof(int); i++)
    {
        std::cout << arr[i] << " ";
    }
    
    

    return 0;
}
