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
        
    

import sys

def main():

    with open('graph_input_00_112.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    for v in range(g.V):
        print('Vertex {} connects to {}'.format(v, g.adj[v]))
    for v in range(V):
        print('Degree of vertex {} is {}'.format(v, g.degree(v)))
    print('Maximum degree is {}'.format(g.maxDegree()))
    print('Average degree is {:.2f}'.format(g.avgDegree()))

if __name__ == '__main__':
    main()