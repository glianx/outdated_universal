# [node, parent, children]
tree = [[0,None,[1,2]],[1,0,[3,4]],[2,0,[5]],[3,1,[6,7]],[4,1,[]],[5,2,[8,9]],[6,3,[]],[7,3,[]],[8,5,[]],[9,5,[]]]

node = tree[0]
stack = []

while True:
    for child in list(reversed(node[2])):
        stack.append(child)
    if stack != []:
        node = tree[stack[-1]]
        stack.pop(-1)
        print(node[0])
    elif stack == []:
        break
