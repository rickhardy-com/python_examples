#from dijkstraInitDict import initiate_empty_dictionary

from dijkstraPathfinder import pathfinder


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
    

    goal = "F"
    shortest_path = get_shortest_path (previous_vertex, start, goal)
    print (shortest_path)
    
