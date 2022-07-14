// clang++ -Wall -std=c++11 bdbfs_oop.cpp -o bdbfs_oop
#include <iostream>
#include <string>
#include <queue>

using namespace std;

class Adjacent_Node {
    public: 
        int vertex;
        Adjacent_Node* next;
};

class Graph_Class {
    public:
        int root;
        int graph_len;

        int n_vertices;
        
        queue<int> src_queue;
        queue<int> dest_queue;

        int *src_visited;
        int *dest_visited;

        int *src_parent;
        int *dest_parent;
        Adjacent_Node graph[12];

        int graph_bool[12];

        Graph_Class(int r, int gl, int nv) {
            root = r;
            graph_len = gl;
            
            n_vertices = nv;
        }

        void add_edge(int src, int dest) {
            Adjacent_Node node;
            node.vertex = dest;
            node.next = &graph[src];
            graph[src] = node;

            graph_bool[src] = true;

            Adjacent_Node node2;
            node2.vertex = src;
            node2.next = &graph[dest];
            graph[dest] = node2;

            graph_bool[dest] = true;
        }

        void bfs(string direction) {
            if (direction == "forward") {
                int current = src_queue.front();
                src_queue.pop();

                Adjacent_Node connected_node = graph[current];
                bool connected_node_bool = graph_bool[current];

                while (connected_node_bool != 0) {
                    int vertex = connected_node.vertex;
                    
                    if (!src_visited[vertex]) {
                        src_queue.push(vertex);
                        src_visited[vertex] = true;
                        src_parent[vertex] = current;
                    }

                    cout << "*" << endl;
                }

                connected_node = *connected_node.next;
                // update connected_node_bool?

            }
        }
};

int main() {
    int r = 0;
    int gl = 8;
    int nv = 12;
    Graph_Class graph_obj(r, gl, nv);
    graph_obj.add_edge(0,4);
    // graph_obj.bfs("forward");
    return 0;
}

