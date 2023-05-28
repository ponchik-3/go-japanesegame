#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <chrono>
#include "classes.h"
#include "io_operators.h"

using namespace std;



int main()
{
    int a = 10;
    string aa = to_string(a);
    cout << aa << "\n";
    /*
    //time since epoch
    uint64_t begin = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    for (int i = 0; i < 1000; i++)
    {
        cout << "aomgus";
    }
    uint64_t end = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    for (int i = 0; i < 10; i++)
    {
        cout << endl;
    }
    cout << "time spent: " << (end - begin)/1000.0 << endl;

    vector<int> f;
    for (int i = 0; i < 4; i++)
    {
        f.push_back(i);
    }
    vector<int> s = f;
    for (int i = 0; i < s.size(); i++)
    {
        cout << s[i] << " ";
    }
    cout << endl;

    cout << stoi("23") << endl;
    string stt = "amoeba";
    cout << stt[2] << endl;

    std::vector<int> first;
    for (int i = 0; i < 5; i++)
    {
        first.push_back(i*2);
    }
    std::vector<int> second;
    second = first;
    second.push_back(-6);
    for (int i = 0; i < first.size(); i++)
    {
        cout << first[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < second.size(); i++)
    {
        cout << second[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < first.size(); i++)
    {
        cout << first[i] << " ";
    }
    cout << endl;*/

    vector<vector<int>> matrix;
    vector<int> row;
    for (int i = 0; i < 10; i++)
    {
        row.clear();
        for (int j = 0; j < 10; j++)
        {
            row.push_back(j*i);
        }
        matrix.push_back(row);
    }

    vector<vector<int>> other;
    other = matrix;
    cout << matrix << "\n\n" << other << "\n\n\n\n";
    other[2][3] = 246;
    cout << matrix << "\n\n" << other << "\n";

    return 0;
}