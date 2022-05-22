// clang++ -Wall -std=c++11 fib_dp_tabu.cpp -o fib_dp_tabu
#include <iostream>
using namespace std;

#define n 40

void _init(int lookup[n]) {
    for (int i = 0; i < n; i++) {
        lookup[i] = 0;
    }
    lookup[1] = 1;
}

int fibo(int lookup[n]) {
    for (int i = 2; i < n + 1; i++) {
        lookup[i] = lookup[i - 1] + lookup[i - 2];
    }
    return lookup[n];
}

int main() {
    // int n = 40;
    int lookup[n];
    _init(lookup);
    cout << fibo(lookup);
}