
# initiate dictionaries with initial values for a* 
def initiate_empty_dictionary (graph, start):
    
     previous_vertex = {}
     distance = {}
     f = {} # distance
      
     infinity = float ("inf")
     for vertex in graph:
         distance[vertex] = infinity
         f[vertex] = infinity
         
     distance[start] = 0
     #f[start] = heuristic[start]
    
     #previous_vertex - empty string 
     return previous_vertex, f, distance
 
    
# find the most likey paths from start to goal
def pathfinder (graph, heuristic, heuristic2, start, goal):
    
    # set up the factored cost trace table ready to calculate
    previous_vertex, factored_cost, distance = initiate_empty_dictionary(graph, start)
    
    # cost of the start vertex can also be calculated in the initiator function,
    # heuristic values need to be passed
    factored_cost[start] = heuristic[start]+heuristic2[start]
        
    while goal in graph:  # A*
        shortest = None 
                
        # This loop is the same as Dijkstra
        for vertex in graph:
            # this forces the first vertex examined to be the shortest
            if shortest == None: 
                shortest = vertex 
            # this compares with the shortest vertex found so far
            elif factored_cost[vertex] < factored_cost[shortest]:
                shortest = vertex
        
        # A* find the neighbour with the lowest cost
        for neighbour, cost in graph[shortest].items():
            if neighbour in graph and cost + distance[shortest] + heuristic[neighbour] + heuristic2[neighbour] < factored_cost[neighbour]:
                
                distance [neighbour] = cost + distance[shortest]
                factored_cost [neighbour] = cost + distance[shortest] + heuristic[neighbour] + heuristic2[neighbour]
                previous_vertex[neighbour] = shortest
          
        graph.pop (shortest)

    return (previous_vertex)

# Trace the path back to the goal
def get_shortest_path (previous_vertex, start, goal):
    shortest_path = []
     
    vertex = goal
    while vertex != start:
        shortest_path.insert (0, vertex)
        vertex = previous_vertex [vertex]
    shortest_path.insert (0,start)
    
    return (shortest_path)
    

if __name__ == "__main__":
    
    
    #the graph as a dictionary of dictionaries  
    graph = {"A": {"B": 4, "C": 3, "D":2}, 
             "B":{"A":4,"E":4}, 
             "C":{"A":3, "D":5}, 
             "D":{"A":2, "C":5, "F":2},
             "E":{"B":4, "G":2},
             "F":{"D":2, "G":10},
             "G":{"E":2, "F":10}
             }
    # heuristic is the cost of visiting each vertex in this example
    tolls = {"A": 10, 
             "B": 16, 
             "C": 8, 
             "D": 1,
             "E": 2,
             "F": 10,
             "G": 0
             }
    congestion_charges = {"A": 10, 
             "B": 0, 
             "C": 0, 
             "D": 500, # this would be different for electric vehicles
             "E": 0,
             "F": 0,
             "G": 0
             }

    start = "A"
    previous_vertex = pathfinder(graph, tolls, congestion_charges, "A", "G")
    
    goal = "G" 
    shortest_path = get_shortest_path (previous_vertex, start, goal)
    print (shortest_path)
    

   
