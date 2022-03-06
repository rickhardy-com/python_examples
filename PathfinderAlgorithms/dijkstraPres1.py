
start = "A"

graph = {"A": {"B": 4, "C": 3, "D":2}, 
         "B":{"A":4,"E":4}, 
         "C":{"A":3, "D":5}, 
         "D":{"A":2, "C":5, "F":2},
         "E":{"B":4, "G":2},
         "F":{"D":2, "G":10},
         "G":{"E":2, "F":10}
         }
    
distance = {} 

previous_vertex = {}

infinity = 9999  # can also use infinity = float ("inf")

for vertex in graph:
     
    distance[vertex] = infinity 
    
distance [start] = 0
 
