
# initiate dictionaries with initial values for a* 
def initiate_empty_dictionary (graph, heuristic, start):
    
     previous_vertex = {}
     distance = {}
     f = {} # distance
      
     infinity = float ("inf")
     for vertex in graph:
         distance[vertex] = infinity
         f[vertex] = infinity
         
     distance[start] = 0
     f[start] = heuristic[start]
    
     #previous_vertex - empty string 
     return previous_vertex, f, distance
 
    
# find the most likey paths from start to goal
def pathfinder (graph, heuristic, start, goal, heuristic_weight):
     
    previous_vertex, factored_cost, distance = initiate_empty_dictionary(graph, heuristic, start)
        
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
            if neighbour in graph and cost + \
                                      distance[shortest]  + \
                                      heuristic[neighbour] * heuristic_weight \
                                      < factored_cost[neighbour]:
                
                distance [neighbour] = cost + distance[shortest]
                factored_cost [neighbour] = cost + distance[shortest] + heuristic[neighbour] * heuristic_weight
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
    graph = {"A": {"B": 400, "C": 30, "D":20}, 
             "B":{"A":40,"E":40}, 
             "C":{"A":30, "D":50}, 
             "D":{"A":20, "C":50, "F":20},
             "E":{"B":40, "G":20},
             "F":{"D":20, "G":100},
             "G":{"E":20, "F":100}
             }
    # heuristic is the cost of visiting each vertex in this example
    heuristic = {"A": 10, 
             "B": 6, 
             "C": 8, 
             "D": 60,
             "E": 2,
             "F": 10,
             "G": 0
             }
    
    heuristic_weight = 7.5 # It is costly to go to D 

    start = "A"
    previous_vertex = pathfinder(graph, heuristic, "A", "G", heuristic_weight)
    
    goal = "G" 
    shortest_path = get_shortest_path (previous_vertex, start, goal)
    print (shortest_path)
    

   
