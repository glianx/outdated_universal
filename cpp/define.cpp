// clang++ -Wall -std=c++11 define.cpp -o define
#include <iostream>
#include <cmath>
using namespace std;

#define X 7
#define Y (2*X+1)
#define fori10 for (int i = 0; i < 10; i++)
#define fori(x) for (int i = 0; i < x; i++)
#define sum_sqrs(a,b) (pow(a,2) + pow(b,2))

int main() {
    cout << X << endl;
    cout << Y << endl;
    fori10 {
        cout << i << endl;
    }
    fori(15) {
        cout << i << endl;
    }
    cout << sum_sqrs(3,4) << endl;
}