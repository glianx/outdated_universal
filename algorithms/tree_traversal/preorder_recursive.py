# [node, parent, children]
tree = [[0,None,[1,2]],[1,0,[3,4]],[2,0,[5]],[3,1,[6,7]],[4,1,[]],[5,2,[8,9]],[6,3,[]],[7,3,[]],[8,5,[]],[9,5,[]]]

def dfs(node):
    if node[2] != []:
        child = tree[node[2][0]]
        node[2].pop(0)
        print(child[0])
        dfs(child)
    if node[2] == []:
        parent = tree[node[1]]
        if parent[0] == 0 and parent[2] == []:
            exit()
        dfs(parent)

dfs(tree[0])