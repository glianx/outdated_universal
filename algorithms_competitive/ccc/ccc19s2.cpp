// clang++ -Wall -std=c++14 ccc19s2.cpp -o ccc19s2
#include <iostream>
#include <math.h>
using namespace std;

bool is_prime(int x) {
    for (int i = 2; i < sqrt(x) + 1; i++) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    cout << endl;
    for (int h = 0; h < T; h++) {
        int N;
        cin >> N;
       
        for (int i = 2; i < N; i++) {
            if (is_prime(i) == true and is_prime(2*N - i) == true) {
                cout << i << " " << 2*N - i << endl;
                break;
            }
        }
    }
}