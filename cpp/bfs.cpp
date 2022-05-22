// clang++ -Wall -std=c++11 bfs.cpp -o bfs
#include <iostream>
#include <queue>

using namespace std;

void bfs(int tree[11][3], int root, int tree_size) {
    queue<int> q;
    q.push(root);

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int i = 0; i < sizeof(tree[v]) / sizeof(int); i++) {
            if (v < tree_size and tree[v][i] != 0) {
                cout << tree[v][i] << " ";
                q.push(tree[v][i]);
            }
        }
    }
}

int main() {
    int tree[11][3] = {{1,2,3},{4,5},{},{6,7},{8,9},{},{10,11}};
    bfs(tree, 0, 8);
    return 0;
}