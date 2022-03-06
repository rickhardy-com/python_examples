from dijkstraInitDict import initiate_empty_dictionary

# Find the shortest distance from start to all vertices
# Populate a dictionary
def pathfinder (graph, start):
    
    # The two dictionaries are complementary, they must have the same top level elements as graph
    previous_vertex = {} # dictionary of previous nodes for this start
    distance = initiate_empty_dictionary (graph, start)
    
    
    

    


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

    print (previous_vertex)
    
