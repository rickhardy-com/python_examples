

import dijk

def pathfinder (graph, start):
    
    #The following two dictionaries could be combined
    distance = {} # dictionary of distances from start
    previous_vertex = {} # dictionary of previous nodes for this start
    
    #initiate up a dictionary of distances from start
    infinity = float ("inf")
    for vertex in graph:
        #print (vertex, graph[vertex])  
        distance[vertex] = infinity 
    distance [start] = 0
    #print ("distance @ start:", distance) 
    
    while graph:
        shortest = None 
                
        # This uses the distance dictionary through all the vertexes left in the graph looking for the shortest
        for vertex in graph:
            # this forces the first vertex examined to be the shortest
            if shortest == None: 
                shortest = vertex 
            # this compares with the shortest vertex found so far
            elif distance[vertex] < distance[shortest]:
                shortest = vertex
        
        for neighbour, cost in graph[shortest].items():
            if neighbour in graph and cost + distance[shortest] < distance[neighbour]:
                
                distance [neighbour] = cost + distance[shortest]
                previous_vertex[neighbour] = shortest
            
        graph.pop (shortest)

    return (previous_vertex)

def get_shortest_path (previous_vertex, start, goal):
    shortest_path = []
     
    vertex = goal
    while vertex != start:
        shortest_path.insert (0, vertex)
        vertex = previous_vertex [vertex]
    shortest_path.insert (0,start)
    
    return (shortest_path)
    


if __name__ == "__main__":
    
    graph = {"A": {"B": 4, "C": 3, "D":2}, 
             "B":{"A":4,"E":4}, 
             "C":{"A":3, "D":5}, 
             "D":{"A":2, "C":5, "F":2},
             "E":{"B":4, "G":2},
             "F":{"D":2, "G":10},
             "G":{"E":2, "F":10}
             }
        
    start = "A"
    previous_vertex = pathfinder(graph, "A")
   
      
    goal = "G" 
    shortest_path = get_shortest_path (previous_vertex, start, goal)
    print (shortest_path)
    
