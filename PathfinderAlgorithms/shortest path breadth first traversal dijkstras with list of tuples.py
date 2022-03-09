#breadth first search
GRAPH = {}

def make_link(Graph, node1,node2):
    """
    A graph will be a dictionary containing nodes.
    These nodes will be a dictionary of neighbour nodes.
    The node's dictionary key will be the neighbour node and
    its value will be 1.
    Return the updated graph.
    """
    if node1 not in Graph:
        Graph[node1] = {}
    Graph[node1][node2] = 1
    if node2 not in Graph:
        Graph[node2] = {}
    Graph[node2][node1] = 1
    return Graph
#end make_link

#breadth first search

def bfs(graph, start):
    visited = []
    queue =  [start]
    i = 0
    while queue:
        
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            
            queue.append(graph[vertex][i])
        
            print('visited',visited, queue)
        i+=1
    return visited

def marked_node(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbour in G[node]:
        total_marked+= marked_node(G, neighbour,marked)
    
#the subroutine list_node_sizes(G) sets up a dictionary to hold marked nodes,
# i.e. the nodes that have been visited.

def list_node_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print("graph containing", node,\
                  ":",marked_node(G,node,marked))

def short_path (G, node1,node2):
    #return shortest path from node1 to node2
    dist_from_start = {}
    queue = [node1]
#    dist_from_start[node1] = 0
    dist_from_start[node1] = [node1]
    while len(queue) > 0:
        current = queue[0]
        del queue[0]
        for neighbour in G[current].keys():                 
            if neighbour not in dist_from_start:
#                dist_from_start[neighbour]= dist_from_start[current]+1
                dist_from_start[neighbour]= dist_from_start[current]+[neighbour]
                if neighbour == node2:
                    return dist_from_start[node2]
                queue.append(neighbour)
    return False

#main
#graph = {'A': ['B', 'C'],
#         'B': ['A', 'D', 'E'],
##         'C': ['A', 'F'],
 #        'D': ['B'],
#         'E': ['B', 'F'],
#         'F': ['C', 'E']}
         
towns = [('A','B'),('A','D'),('A','E'),
         ('B','A'),('B','C'),('B','D'),
         ('C','B'),('C','G'),
         ('D','A'),('D','B'),('D','E'),('D','F'),
         ('E','A'),('E','D'),('E','F'),         
         ('F','D'),
         ('G','C')]
#traversal = bfs(graph, 'A') # {'B', 'C', 'A', 'F', 'D', 'E'}
#print(traversal)
for (x,y) in towns:
    make_link(GRAPH,x,y)
print (short_path(GRAPH,'E','G'))