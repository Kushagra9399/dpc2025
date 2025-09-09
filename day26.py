'''
You are given an undirected graph represented by an adjacency list. Your task is to determine if the graph contains any cycle.
A cycle is formed if you can traverse through a sequence of edges that starts and ends at the same vertex, with at least one edge in between.
Input:
An integer V representing the number of vertices in the graph.
A list of edges, where each edge connects two vertices of the graph.
Output:
Return true if the graph contains a cycle, otherwise return false.
Examples:
Example 1
Input: V = 5, Edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
Output: true
Explanation: The edges form a cycle: 0 → 1 → 2 → 3 → 4 → 0.
'''
def detect_cycle(v, visited, curr, parent, l):
    visited[curr] = True
    for i in range(v):
        if l[curr][i] == 1:
            if not visited[i]:
                if detect_cycle(v, visited, i, curr, l):
                    return True
            elif i != parent:
                return True
    return False

def day26_sol(v, edges):
    if not edges:
        return False
    l = [[0]*v for _ in range(v)]
    for u, w in edges:
        l[u][w] = 1
        l[w][u] = 1
    visited = [False]*v
    for i in range(v):
        if not visited[i]:
            if detect_cycle(v, visited, i, -1, l):
                return True
    return False

print(day26_sol(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]))
