// clang++ -Wall -std=c++11 test.cpp -o test
#include <iostream>
#include <string>
#include <queue>

using namespace std;

void bfs(int tree[8][3]) {
    queue<int> Q;
    Q.push(3);
    Q.push(4);
    Q.push(5);
    for (int i = 0; i < 3; i++) {
        cout << Q[i]
    }
}

int main() {
    int tree[8][3] = {{1,2,3},{4,5},{},{6,7},{8,9},{},{10,11},{}};
    bfs(tree);
    return 0;
}