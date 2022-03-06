


def find_shortest(vertex_info):
    for vertex in graph:
        # this sets the first vertex examined to be the shortest
        if shortest == None:
            shortest = vertex
        # this checks for shorter ones
        elif vertex_info[vertex][0] < vertex_info[shortest][0]:
            shortest = vertex


# Calculates the previous vertex for every vertex in the graph and outputs a dictionaryfor the start node
# This is the part that is often pre-calculated in map applications
def pathfinder (graph, start):
    print (graph)
    
    # initiate a single dictionary of distances from start and previous vertex 
    vertex_info = {} 
    infinity = float ("inf")
    for vertex in graph:
        vertex_info[vertex]=[infinity, ""]
    vertex_info[start]=[0, ""]
    
    
    while graph:
        shortest = None 
        
        # This uses the graph dictionary to go through all the vertexes remaining 
        # shortest stores the shortest path found so far
        # this decides which vertex will be calculated first
        
        for vertex in graph:
            # this sets the first vertex examined to be the shortest
            if shortest == None:
                shortest = vertex
            # this checks for shorter ones
            elif vertex_info[vertex][0] < vertex_info[shortest][0]:
                shortest = vertex
        
        # for the vertex returned by the previous loop
        for neighbour, cost in graph[shortest].items():
            if neighbour in graph and cost + vertex_info[shortest][0] < vertex_info[neighbour][0]:
                vertex_info [neighbour] = [cost + vertex_info[shortest][0], shortest]
                
        graph.pop (shortest) #visited nodes are removed from the graph
    return vertex_info

def get_shortest_path (vertex_info, start, goal):
    shortest_path = []
    

    
    vertex = goal
    total_cost = 0
    
    while vertex != start:
        shortest_path.insert (0, vertex)
        total_cost += vertex_info[vertex][0]
        vertex = vertex_info [vertex][1]
        
        
    shortest_path.insert (0,start)
    
    return (shortest_path, total_cost)

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
    print ('PREV VERTEX', previous_vertex)
    

    goal = "G" 
    shortest_path, total_cost = get_shortest_path (previous_vertex, start, goal)
    print (start," to " ,goal ,shortest_path)
    print (total_cost)
    

