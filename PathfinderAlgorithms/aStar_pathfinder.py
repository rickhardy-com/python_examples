

from astarinit import initiate_empty_dictionary

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
        
        # A*
        for neighbour, cost in graph[shortest].items():
            if neighbour in graph and cost + distance[shortest] + heuristic[neighbour] < factored_cost[neighbour]:
                
                distance [neighbour] = cost + distance[shortest]
                factored_cost [neighbour] = cost + distance[shortest] + heuristic[neighbour]
                previous_vertex[neighbour] = shortest
          
        graph.pop (shortest)

    return (previous_vertex)



    
