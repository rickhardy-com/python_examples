
# Find the shortest distance from start to all vertices
# Populate a dictionary
def pathfinder (graph, start):
    
    # The two dictionaries are complementary, they must have the same top level elements as graph
    previous_vertex = {} # dictionary of previous nodes for this start
    distance = initiate_empty_dictionary (graph, start)
    
    while graph:
        shortest = None 
        
        # C&D p208 2a. Find the vertex with shortest dist from start not visited        
        # This uses the distance dictionary through all the vertexes left in the graph looking for the shortest
        # Vertexes that have already been visited are no longer in the graph!
        for vertex_check in graph:
            # this forces the first vertex examined to be the shortest
            if shortest == None: 
                shortest = vertex_check 
            # this compares with the shortest vertex found so far and replaces it if necessary
            elif distance[vertex_check] < distance[shortest]:
                shortest = vertex_check
        
        for neighbour, cost in graph[shortest].items():
            
            if neighbour in graph and cost + distance[shortest] < distance[neighbour]:
                
                distance [neighbour] = cost + distance[shortest]
                previous_vertex[neighbour] = shortest
            
        graph.pop (shortest) # Visited!

    return (previous_vertex)

    


if __name__ == "__main__":  
    
    from dijkstraInitDict import initiate_empty_dictionary
    
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

    print (previous_vertex)
    
