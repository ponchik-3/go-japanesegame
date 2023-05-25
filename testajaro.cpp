#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <chrono>

using namespace std;



int main()
{
    int a = 10;
    string aa = to_string(a);
    cout << aa << "\n";

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
    return 0;
}