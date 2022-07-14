tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]

def dfs_recursive(tree,v):
    print(v)
    if v <= 6:
        for c in tree[v]:
            dfs_recursive(tree,c)

dfs_recursive(tree,0)