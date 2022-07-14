// clang++ -Wall -std=c++11 ccc17s2.cpp -o ccc17s2
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    int tides[N];
    for (int i = 0; i < N; i++) {
        int tide;
        cin >> tide;
        tides[i] = tide;
    }
    sort(tides,tides + N);

    if (N % 2 == 0) {
        for (int j = 0; j < N / 2; j++) {
            cout << tides[N / 2 - j - 1] << " ";
            cout << tides[N / 2 + j] << " ";
        }
    }

    else {
        cout << tides[(N - 1) / 2] << " ";
        for (int k = 0; k < (N - 1) / 2; k++) {
            cout << tides[(N - 1) / 2 - k - 1] << " ";
            cout << tides[(N - 1) / 2 + k + 1] << " ";
        }
    }
}