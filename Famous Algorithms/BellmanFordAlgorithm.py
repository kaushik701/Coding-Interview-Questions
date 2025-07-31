def bellman_ford(graph, source):
    # Step 1: Initialize distances from source to all vertices as infinity
    # and distance to source as 0
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    
    # Get all edges from the graph
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))
    
    # Step 2: Relax all edges |V| - 1 times
    # V is the number of vertices
    V = len(graph)
    for _ in range(V - 1):
        for u, v, weight in edges:
            # Relaxation step
            if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Step 3: Check for negative weight cycles
    # If we can still relax edges, then we have a negative weight cycle
    negative_cycle = False
    for u, v, weight in edges:
        if distances[u] != float('infinity') and distances[u] + weight < distances[v]:
            negative_cycle = True
            distances[v] = float('-infinity')  # Mark vertices affected by negative cycles
    
    return distances, negative_cycle