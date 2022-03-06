
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
def pathfinder (graph, heuristic, start, goal):
     
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
            if neighbour in graph and cost + distance[shortest] + heuristic[neighbour] < factored_cost[neighbour]:
                
                distance [neighbour] = cost + distance[shortest]
                factored_cost [neighbour] = cost + distance[shortest] + heuristic[neighbour]
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
    heuristic = {"A": 10, 
             "B": 6, 
             "C": 8, 
             "D": 12,
             "E": 2,
             "F": 10,
             "G": 0
             }
    start = input ('start vertex: ')
    #start = "A"
    previous_vertex = pathfinder(graph, heuristic, "A", "G")
    
    goal = input ('end vertex: ')
    #goal = "G" 
    shortest_path = get_shortest_path (previous_vertex, start, goal)
    print (shortest_path)
    
# Challenges and NEA topics:
'''
return the distance travelled for the route (and/or total cost of route)
add a weight to the heuristic to make it more or less likely to be taken
add a second heuristic
'''
    

   
