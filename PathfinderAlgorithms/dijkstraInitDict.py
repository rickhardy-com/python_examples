# Initiates an empty dictionary

def initiate_empty_dictionary (graph, start):
    
    distance = {} # dictionary of distances from start
    
    #initiate up a dictionary of distances from start
    infinity = float ("inf")
    for vertex in graph:
        #print (vertex, graph[vertex])  
        distance[vertex] = infinity 
    distance [start] = 0
    #print ("distance @ start:", distance) 
    return distance