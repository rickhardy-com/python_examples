# Initiates an empty dictionary

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
 
    


