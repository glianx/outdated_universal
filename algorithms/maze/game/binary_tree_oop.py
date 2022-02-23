import random
import time
import os

class Pixel:
    def __init__(self,type,colour,visible,y,x,explored,expanded):
        self.type = type
        self.colour = colour
        self.visible = visible
        self.y = y
        self.x = x
        self.explored = explored
        self.expanded = expanded

def create_graph(n):
    graph = []
    for y in range(n):
        pixel_row = []
        for x in range(n):
            if x % 2 == 0 and y % 2 == 0: type = 'node'
            if x % 2 == 1 and y % 2 == 1: type = 'blank'
            if (x + y) % 2 == 1: type = 'non-edge'
            
            pixel = Pixel(type = type,
                        colour = white,
                        visible = False,
                        y = y,
                        x = x,
                        explored = 0,
                        expanded = False)
            pixel_row.append(pixel)
        graph.append(pixel_row)
            
    return graph

def render(finished = False):
    os.system('clear')
    for y in range(n):
        for x in range(n):
            node = graph[y][x]
            if finished == False:
                if node.type == 'node' or node.type == 'edge':
                    node.colour = none
                if node.type == 'non-edge' or node.type == 'blank':
                    node.colour = white
                if node.type == 'player':
                    node.colour = green
            elif finished == True:
                if node.type == 'node' or node.type == 'edge':
                    if node.explored > 0:
                        node.colour = red 
                    elif node.expanded == True:
                        node.colour = green
            if node.visible == True:
                
                print(node.colour,end = '')
            else:
                print('  ', end = '')
        print()


def binary_tree():
    for y in range(0,n,2):
        for x in range(0,n,2):
            if y == 0 and x == 0:
                pass
            elif y == 0:
                graph[y][x-1].type = 'edge'
            elif x == 0:
                graph[y-1][x].type = 'edge'
            else:
                dy, dx = random.choice([[-1,0],[0,-1]])
                graph[y+dy][x+dx].type = 'edge'

n = 21
none, white, green, red, orange = '  ','⬜','🟩','🟥','🟧'
graph = create_graph(n)

binary_tree()
render()

# ----------------------------------------------------------------------

r = 5
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def around(y,x,r):
    around_pos = [(y+a,x+b) for a in range(-r,r+1,1) for b in range(-r,r+1,1)]
    return [[a,b] for [a,b] in around_pos if 0 <= a <= n-1 and 0 <= b <= n-1]

y,x = 0,0
prev_type = graph[y][x].type

start = time.time()


while True:

    if [y,x] == [n-1,n-1]:
        graph[y][x].explored = 1
        break

    input_ = _Getch()()

    # set surrounding nodes to invisible
    graph[y][x].type = 'edge'
    for [a,b] in around(y,x,r):
        graph[a][b].visible = False

    # change y,x with arrow keys
    if input_ == '\x1b[A':
        if y != 0 and graph[y-1][x].type in ['node','edge']:
            y -= 1
    elif input_ == '\x1b[B':
        if y != n-1 and graph[y+1][x].type in ['node','edge']:
            y += 1
    elif input_ == '\x1b[C':
        if x != n-1 and graph[y][x+1].type in ['node','edge']:
            x += 1
    elif input_ == '\x1b[D':
        if x != 0 and graph[y][x-1].type in ['node','edge']: 
            x -= 1

    # set surrounding nodes to visible
    for [a,b] in around(y,x,r):
        graph[a][b].visible = True
        graph[a][b].expanded = True

    # make current node visible and colour green
    graph[y][x].visible = True
    graph[y][x].type = 'player'
    graph[y][x].explored += 1
    render()

# set all visible
for row in graph:
    for node in row:
        node.visible = 1

render(finished = True)

runtime = time.time() - start
explored = 0
expanded = 0
steps = 0

for y in range(n):
    for x in range(n):
        node = graph[x][y]
        explored += int(bool(node.explored))
        expanded += int(node.expanded) - int(bool(node.explored))
        steps += node.explored

print('runtime:', runtime)
print('explored',explored)
print('expanded',expanded)
print('steps',steps)
input()