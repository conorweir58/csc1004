#!/usr/bin/env python3

class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for V in range(self.V):
            self.adj[V] = list()
    
    def addEdge(self, V, w):
        self.adj[V].append(w)
        self.adj[w].append(V)
    
    def degree(self, V):
        return len(self.adj[V])
    
    def maxDegree(self):
        return len(max(self.adj.values(), key=len))
    
    def avgDegree(self):
        total = [len(n) for n in self.adj.values()]
        avg = sum(total) / len(total)
        return(round(avg, 2))

class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
        self.dfs(s)
    
    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)
    
    def hasPathTo(self, v):
        return(self.visited[v])
    
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]


#!/usr/bin/env python3

import sys

def main():

    with open('graph_input_00_112.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    dfs = DFSPaths(g, 4)

    print(dfs.hasPathTo(2))

    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()