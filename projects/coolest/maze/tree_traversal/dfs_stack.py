tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]]

def dfs_stack(tree,r,d):
    S = [r]
    while S != []:
        n = S.pop()
        print(n)
        if n == d: 
            break
        if n <= 6:
            for c in tree[n]:
                S.append(c)

dfs_stack(tree,0,4)