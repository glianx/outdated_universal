// clang++ -Wall -std=c++11 bdbfs.cpp -o bdbfs
#include <iostream>
#include <queue>
using namespace std;
#define N 8
#define B 3

void bfs(int tree[N][B], int root, int tree_len) {
    queue<int> q;
    q.push(root);

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int i = 0; i < lenof(tree[v]) / lenof(int); i++) {
            if (v < tree_len and tree[v][i] != 0) {
                cout << tree[v][i] << " ";
                q.push(tree[v][i]);
            }
        }
    }
}

// void bdbfs(int tree[N][B])

int main() {
    int tree[N][B] = {{1,2,3},{4,5},{},{6,7},{8,9},{},{10,11}};
    bfs(tree, 0, N);
    return 0;
}