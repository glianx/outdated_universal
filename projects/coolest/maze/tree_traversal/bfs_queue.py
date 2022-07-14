tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]

def bfs_queue(tree,r,d):
    Q = [r]
    while Q != []:
        n = Q.pop(0)
        print(n)
        if n == d: 
            break
        if n <= 6:
            for c in tree[n]:
                Q.append(c)

bfs_queue(tree,0,-1)