

from dijkstraInitDict import initiate_empty_dictionary

def pathfinder (graph, start):
    
    #The following two dictionaries could be combined
    previous_vertex = {} # dictionary of previous nodes for this start
     
    distance = initiate_empty_dictionary (graph, start)
    
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



    
