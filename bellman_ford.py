def bellman_ford(graph, start):
    """An algorithm to check for the shortest path and to check for any negative cycles
        Input:  A graph and a source vertex
        Output: The shortest path from source node to all other vertices or an error message saying a negative cycle had been found
        Time complexity:
        Space complexity:

    """
#Initialise
    distance = [math.inf] * (len(graph)+1)
    pred = [None] * (len(graph)+1)
    distance[start] = 0
    error = "Negative edge cycle found in the graph"

#Iteratively estimate dist[v] from source s
    v = 1
    for i in range(len(graph)-2):
        for u in range(len(graph) - 1):
            for v in range(len(graph) - 1):
                est = dist[u] + dist[u][v]
                if est < dist[v]:
                    dist[v] = est
                    pred[v] = u

#Checks and returns false if any negative weight cycle is along the path from s o any other vertex
    k = 1
    for j in range(len(graph)-1):
        for k in range(len(graph)-1):
            if dist[j] + graph[j][k] < dist[k]:
                return error

    return distance, pred
