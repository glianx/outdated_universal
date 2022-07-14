class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def min_key(self, mst_set, keys):
        curr_min_key = float('inf')
        for i in range(len(keys)):
            if keys[i] < curr_min_key and mst_set[i] == False:
                curr_min_key = keys[i]
                curr_min_index = i
        return curr_min_index

    def print_mst(self, parents):
        print('\nEdge \tWeight')
        for v in range(1, len(parents)):
            print(parents[v], '-', v, '\t', self.graph[parents[v]][v])
    
    def prims(self):
        mst_set = [False] * self.V
        keys = [float('inf')] * self.V
        parents = [None] * self.V

        keys[0] = 0
        parents[0] = -1

        for _ in range(self.V):

            u = self.min_key(mst_set, keys)
            mst_set[u] = True

            for v in range(self.V):
                # adjacent, unexplored, optimal
                new_key = self.graph[u][v]
                if new_key != 0 and mst_set[v] == False and new_key < keys[v]:
                    keys[v] = new_key
                    parents[v] = u
        
        self.print_mst(parents)

g = Graph(5)
g.graph =  [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
g.prims()