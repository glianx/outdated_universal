import random
import time
import os

class Pixel:
    def __init__(self,type,colour,visible,y,x,explored,expanded,set = 0):
        self.type = type
        self.colour = colour
        self.visible = visible
        self.y = y
        self.x = x
        self.yx = (y,x)
        self.explored = explored
        self.expanded = expanded
        self.set = set

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

    for y in range(n):
        for x in range(n):
            node = graph[y][x]
            if finished == False:
                if node.type == 'node':
                    node.colour = str(node.set) + ' '
                    # node.colour = none
                if node.type == 'edge':
                    node.colour = none
                if node.type == 'non-edge' or node.type == 'blank':
                    node.colour = white
            if node.visible == True:   
                print(node.colour,end = '')
            else:
                print('  ', end = '')
        print()

def frame():
    render()
    print()


def set_all_visible():
    for y in range(n):
        for x in range(n):
            graph[y][x].visible = True

# ----------------------------------------------------------------------

def initialize_first_row():
    for x in range(int(n/2)+1):
        node = graph[0][2*x]
        node.set = x + 1

def merge_nodes(y):
    global sets
    sets = [[(y,0)]]
    for x in range(0,n-2,2):
        node = graph[y][x]
        edge = graph[y][x+1]
        next_node = graph[y][x+2]

        if next_node.set != node.set:
            if random.choice((0,1)) == 1:
                # next_node.set = min(node.set,next_node.set)
                # node.set = min(node.set,next_node.set)
                for x2 in range(0,n,2):
                    node2 = graph[y][x2]
                    if node2.set == next_node.set:
                        node2.set = node.set
                        sets[-1].append(node2.yx)
                edge.type = 'edge'


                # add to same set
                # sets[-1].append(next_node.yx)
                frame()

            else:
                # create new set 
                sets.append([next_node.yx])
            

def vertical_connections(y):
    for set in sets:
        random_node_yx = random.choice(set)
        edge_x = random_node_yx[1]

        graph[y+2][edge_x].set = graph[y][edge_x].set
        graph[y+1][edge_x].type = 'edge'
        set.append(graph[y+2][edge_x].yx)

        for yx in set:
            if random.choice((0,0,1)) == 1:
                edge_x = yx[1]
                graph[y+2][edge_x].set = graph[y][edge_x].set
                graph[y+1][edge_x].type = 'edge'
                set.append(graph[y+2][edge_x].yx)                
    sets.append([(y+2,0)])

def initialize_remander_row(y):
    for x in range(0,n,2):
        node = graph[y+2][x]
        if node.set == 0: # 0 is null value
            node.set = max([node.set for node in graph[y+2]]) + 1
    
def merge_last_row():
    for x in range(0,n-2,2):
        node = graph[n-1][x]
        edge = graph[n-1][x+1]
        next_node = graph[n-1][x+2]

        if next_node.set != node.set:
            next_node.set = node.set
            edge.type = 'edge'

def ellers_algorithm():
    initialize_first_row()
    merge_nodes(y = 0) 

    for y in range(0,n-2,2):
        frame()

        vertical_connections(y)

        frame()

        initialize_remander_row(y)

        frame()
        merge_nodes(y+2)
    
    merge_last_row()




n = 9
none, white, green, red, orange = '  ','⬜','🟩','🟥','🟧'
# white, none,  green, red, orange = '  ','⬜','🟩','🟥','🟧'

graph = create_graph(n)

set_all_visible()
ellers_algorithm()
render()
