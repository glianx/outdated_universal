// clang++ -Wall -std=c++11 fib.cpp -o fib
#include <iostream>
using namespace std;

int fibo(int n) {
    if (n <= 1) {
        return n;
    }
    return fibo(n - 1) + fibo(n - 2);
}

int main() {
    cout << fibo(400);
    return 0;
}