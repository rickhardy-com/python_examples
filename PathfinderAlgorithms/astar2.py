

from astarinit import initiate_empty_dictionary

def pathfinder (graph, heuristic, start, goal):
     
    previous_vertex, f,g = initiate_empty_dictionary(graph, heuristic, start)
        
    while goal in graph:
        shortest = None 
                
        # This uses the distance dictionary through all the vertexes left in the graph looking for the shortest
        for vertex in graph:
            # this forces the first vertex examined to be the shortest
            if shortest == None: 
                shortest = vertex 
            # this compares with the shortest vertex found so far
            elif f[vertex] < f[shortest]:
                shortest = vertex
        
        for neighbour, cost in graph[shortest].items():
            if neighbour in graph and cost + g[shortest] + heuristic[neighbour] < f[neighbour]:
                
                g [neighbour] = cost + g[shortest]
                f [neighbour] = cost + g[shortest] + heuristic[neighbour]
                previous_vertex[neighbour] = shortest
          
        graph.pop (shortest)

    return (previous_vertex)



    
