// clang++ -Wall -std=c++11 fib_dp_memo.cpp -o fib_dp_memo
#include <iostream>
using namespace std;

#define NIL -1
#define MAX 800

int lookup[MAX];

void _init(int lookup[MAX]) {
    for (int i = 0; i < MAX; i++) {
        lookup[i] = -1;
    }
}

int fibo(int n) {
    if (lookup[n] == NIL) {
        if (n <= 1) {
            lookup[n] = n;
        }
        else {
            lookup[n] = fibo(n - 1) + fibo(n - 2);
        }
    }
    return lookup[n];
}

int main() {
    _init(lookup);
    cout << fibo(400);
    return 0;
}