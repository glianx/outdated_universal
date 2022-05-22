// clang++ -Wall -std=c++11 bool.cpp -o bool
#include <iostream>

using namespace std;

int main() {
    bool x = true;
    bool y = false;
    bool a = 1;
    bool b = 0;
    bool c = "yes";
    bool d = "";
    bool e[] = {0,1};
    bool f = {};

    cout << x << endl;
    cout << y << endl;
    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    cout << d << endl;
    cout << e << endl;
    cout << f << endl;

    if (c) {cout << 'c';}
    if (d) {cout << 'd';}
    if (e) {cout << 'e';}
    if (f) {cout << 'f';}
    return 0;
}