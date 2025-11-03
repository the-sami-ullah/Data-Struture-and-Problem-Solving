def bellman_ford(n, edges, src):
    # Step 1: Initialize distance for all nodes
    dist = [float('inf')] * n
    dist[src] = 0   # Distance to source is always 0

    # Step 2: Relax all edges (n - 1) times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Graph contains a negative weight cycle")
            return None

    # Step 4: Return shortest distances
    return dist
