'''
You are given an unweighted graph represented by an adjacency list. Your task is to find the shortest path (in terms of the number of edges) between two given nodes in the graph.
Input:
An integer V representing the number of vertices in the graph.
A list of edges, where each edge connects two vertices of the graph.
Two integers, start and end, representing the source and destination nodes respectively.
Output:
Return the shortest path length (number of edges) from start to end. If there is no path, return -1.
'''
def day27_sol(v, edges, start, end):
    l = [[0]*v for _ in range(v)]
    for i in edges:
        l[i[0]][i[1]] = 1
        l[i[1]][i[0]] = 1
    visited = [False]*v
    dist = [float('inf')]*v
    arr = [start]
    visited[start] = True
    dist[start] = 0
    while arr:
        curr = arr.pop(0)
        if curr == end:
            return dist[curr]
        for i in range(v):
            if l[curr][i] == 1 and not visited[i]:
                visited[i] = True
                dist[i] = dist[curr] + 1
                arr.append(i)
    return -1
    
print(day27_sol(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], 0, 4))
