// clang++ -Wall -std=c++11 ccc15s3.cpp -o ccc15s3
#include <iostream>
using namespace std;

bool Pi_docked;

int main() {
    int G;
    // cin >> G;
    G = 4;

    int P;
    // cin >> P;
    P = 3;

    int Gi_docked[] = {0};

    int G0;
    // cin >> G0;
    G0 = 4;

    Gi_docked[0] = G0;

    int Gates[3] = {-1,1,1};

    for (int i = 1; i < P; i++) {
        int Gi;
        // cin >> Gi;
        Gi = Gates[i];

        for (int Gj = Gi; Gj > 0; Gj--) {
            bool Gj_taken = find(begin(Gi_docked), end(Gi_docked), Gj) != end(Gi_docked);
            Pi_docked = false;

            if (Gj_taken == false) {
                Gi_docked[i] = Gj;
                Pi_docked = true;
                break;
            }
        }
        
        if (Pi_docked == false) {
            cout << "airport full: " << i - 1;
        }

    }
}