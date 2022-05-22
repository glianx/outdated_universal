// clang++ -Wall -std=c++11 bfs_oop.cpp -o bfs_oop
#include <iostream>
#include <queue>

using namespace std;

class Graph_Class {
    public:
        int graph_arr[8][3] = {{1,2,3},{4,5},{},{6,7},{8,9},{},{10,11}};
        int root;
        int graph_size;

        Graph_Class(int r, int gs) {
            root = r;
            graph_size = gs;
        }
};

int main() {
    Graph_Class graph(0, 8);
    cout << &graph << endl;
    cout << graph.root << endl;
    cout << &graph.graph_arr << endl;
    cout << graph.graph_arr[0][2] << endl;
    return 0;
}