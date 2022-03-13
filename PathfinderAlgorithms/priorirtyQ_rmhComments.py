from queue import PriorityQueue # essentially a binary heap
import copy

def dijkstra(G, start):
    """ Uniform-cost search / dijkstra """
    visited = set() # empty set, use list to show order
    cost_from_start = {start: 0} # dictionary of shortest distances from start
    previous_vertex = {start: None} # dictionary of previous nodes
    
    # initiate a priority Q
    todo = PriorityQueue()
    todo.put((0, start))
    print ('initial contents of Q:')
    for i in todo.queue:
        print ('   ',i)
    
    
    while not todo.empty():
        print ('length of q before pop',todo.qsize())
        print ('contents of Q:', todo.queue)
        
        _, vertex = todo.get() # finds lowest cost vertex
        print ('popping first priority vertex:' , vertex, 'from the q')
        print ('length of q after pop ',todo.qsize())
        
        # go through each neighbour vertex
        print ('go through all neighbour vertices', G[vertex])
        for neighbor, neighbor_distance in G[vertex]:
            print ('--------------------------')
            print ('looking at neighbour ',neighbor, neighbor_distance)
            if neighbor in visited: 
                print (neighbor, 'has been visited so skip')
                continue # skip these to save time      
            print (neighbor, 'not visited so check distance from start via current node')
            old_cost = cost_from_start.get(neighbor, float('inf')) # default to infinity
            new_cost = cost_from_start[vertex] + neighbor_distance
            print ('comparing distances ', neighbor, 'old:', old_cost, 'new:', new_cost)
            if new_cost < old_cost:
                print ('changing') 
                todo.put((new_cost, neighbor))
                print ('adding to Q :   ', new_cost, neighbor)
                print ('contents of Q:', todo.queue)
                cost_from_start [neighbor] = new_cost
                print ('set distance from start for: ', neighbor, 'to', new_cost)
                print ('known distances from start', cost_from_start)
                previous_vertex[neighbor] = vertex
                print ('previous_vertices', previous_vertex)
                
        print ('adding vertex', vertex, 'to visited')
        visited.add(vertex) #add to visited  list
        
    print ('ending')
    print ('visited list ',visited)
    print ('previous vertex dict: ',previous_vertex)
    print ('costs from start', cost_from_start)
    return previous_vertex

def make_path(previous_vertex, goal):
    if goal not in previous_vertex:
        return None
    v = goal
    path = []
    while v is not None: # root has null previous_vertex
        path.append(v)
        v = previous_vertex[v]
    return path[::-1]


## Example
'''
G = { # random example graph
 'A': {('C', 76)},
 'B': {('C', 20), ('J', 78)},
 'C': {('C', 62), ('F', 99), ('G', 72), ('H', 40)},
 'D': {('A',  8), ('G', 71), ('I', 61)},
 'E': {('C', 16), ('E', 54), ('I',  3)},
 'F': {('J', 66)},
 'G': {('B', 92), ('E', 48), ('G', 31)},
 'H': {('G', 36)},
 'I': {('J', 88), ('K', 16)},
 'J': {('H',  4), ('K', 46)},
 'K': {('I', 40)}
}'''

G = {"A": {("B", 4), ("C",  3), ("D", 2)}, 
         "B":{("A",4), ("E",4)}, 
         "C":{("A",3), ("D",5)}, 
         "D":{("A",2), ("C",5), ("F",2)},
         "E":{("B",4), ("G",2)},
         "F":{("D",2), ("G",10)},
         "G":{("E",2), ("F",10)}
         }

previous_vertex = dijkstra(G, 'A')
print(make_path(previous_vertex, 'G'))

# -> ['A', 'C', 'G', 'E', 'I', 'K']
