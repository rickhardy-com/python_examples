
def initiate_empty_dictionary ():
    vertex_info = {} 
    infinity = float ("inf")
    for vertex in graph:
        vertex_info[vertex]=[infinity, ""]
    vertex_info[start]=[0, ""]
    return (vertex_info)


# This uses the graph dictionary to go through all the remaining vertexes 
#    and returns the next 
# current_vertex stores the current_vertex path found so far
def find_next_vertex (vertex_info, graph):
    current_vertex = None
    for check_vertex in graph:
        # this sets the first vertex examined to be the current_vertex
        if current_vertex == None:
            current_vertex = check_vertex
        # this checks for shorter ones
        elif vertex_info[check_vertex][0] < vertex_info[current_vertex][0]:
            current_vertex = check_vertex
    return current_vertex

# Calculates the previous vertex for every vertex in the graph and outputs a dictionaryfor the start node
# This is the part that is often pre-calculated in map applications
def pathfinder (graph, start):
    
    # Initiate a dictionasry containing default values
    vertex_info = initiate_empty_dictionary ()
    
    
    while graph:
        
        # this decides which vertex will be calculated next (current_vertex)
        current_vertex = find_next_vertex (vertex_info, graph)
        
        # for the vertex returned by the previous loop
        for neighbour, cost in graph[current_vertex].items():
            # if neighbour is no longer in the graph then dont check
            #otherwise check if cost is less and replace the cost and previous node if it is
            if neighbour in graph and cost + vertex_info[current_vertex][0] < vertex_info[neighbour][0]:
                vertex_info [neighbour] = [cost + vertex_info[current_vertex][0], current_vertex]
                
        graph.pop (current_vertex) #visited nodes are removed from the graph
        
    return vertex_info


def get_path_for_goal (vertex_info, start, goal):
    current_vertex_path = [] 
    vertex = goal
    total_cost = 0
    
    while vertex != start:
        current_vertex_path.insert (0, vertex)
        total_cost += vertex_info[vertex][0]
        vertex = vertex_info [vertex][1]
               
    current_vertex_path.insert (0,start)
    
    return (current_vertex_path, total_cost)

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
    paths_from_start = pathfinder(graph, "A")
    print ('Paths from position:', start, "   Paths:", paths_from_start)
    
    # Use the paths_from_start dictionary to find the path to a specified goal
    # Can be used for more than one goal
    goal = "G" 
    current_vertex_path, total_cost = get_path_for_goal (paths_from_start , start, goal)
    print (start," to " ,goal ,current_vertex_path)
    print (total_cost)
    
    goal = "F" 
    current_vertex_path, total_cost = get_path_for_goal (paths_from_start , start, goal)
    print (start," to " ,goal ,current_vertex_path)
    print (total_cost)
    