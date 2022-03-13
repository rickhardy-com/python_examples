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
        
    while not todo.empty():
   
        _, vertex = todo.get() # finds lowest cost vertex

        # go through each neighbour vertex
        for neighbor, neighbor_distance in G[vertex]:

            if neighbor in visited: 
                continue # skip these to save time      
            
            old_cost = cost_from_start.get(neighbor, float('inf')) # default to infinity
            new_cost = cost_from_start[vertex] + neighbor_distance
            
            if new_cost < old_cost:
                 
                todo.put((new_cost, neighbor))
                
                cost_from_start [neighbor] = new_cost

                previous_vertex[neighbor] = vertex

        visited.add(vertex) #add to visited  list
        
    return previous_vertex

def make_path(previous_vertex, goal):
    if goal not in previous_vertex:
        return None
    v = goal
    path = []
    while v is not None: # root has null previous_vertex
        path.append(v)
        v = previous_vertex[v]
        
    # return the list in reverse
    return path[::-1]


## Example

G = { # direceted, weighted graph example
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
}
'''
G = { # undirected weighted graph example
         "A": {("B", 4), ("C",  3), ("D", 2)}, 
         "B":{("A",4), ("E",4)}, 
         "C":{("A",3), ("D",5)}, 
         "D":{("A",2), ("C",5), ("F",2)},
         "E":{("B",4), ("G",2)},
         "F":{("D",2), ("G",10)},
         "G":{("E",2), ("F",10)}
         }'''

previous_vertex = dijkstra(G, 'A')
print(make_path(previous_vertex, 'K'))

# -> ['A', 'C', 'G', 'E', 'I', 'K']
