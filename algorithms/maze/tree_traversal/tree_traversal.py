class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPreorder(root):
    if root:
        print(root.val, end = ' '),
        printPreorder(root.left)
        printPreorder(root.right)

def printInorder(root):
    if root: 
        printInorder(root.left) 
        print(root.val, end = ' '), 
        printInorder(root.right)
 
def printPostorder(root): 
    if root: 
        printPostorder(root.left)
        printPostorder(root.right) 
        print(root.val, end = ' '),
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)


print('\nPreorder: Root, Left, Right')
printPreorder(root)
 
print('\nInorder: Left, Root, Right')
printInorder(root)
 
print('\nPostorder: Left, Right, Root')
printPostorder(root)
