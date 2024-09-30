class Graph(object):
	"""docstring for Graph"""
	def __init__(self, V):
		self.V = V
		self.adj = {}
		for V in range(self.V):
			self.adj[V] = list()

	def addEdge(self, V, w):
		self.adj[V].append(w)
		self.adj[w].append(V)
		
class DFSIslands(object):

	def __init__(self, g, s):
		self.s = s
		self.g = g
		self.visited = [False] * g.V
		self.parent = [-1] * g.V
	
	def dfs(self, v):
		if self.visited != []:
			self.visited[v] = True
			for w in self.g.adj[v]:
				if not self.visited[w]:
					self.parent[w] = v
					self.dfs(w)
	
def count_islands(graph, start=0):
	count = 0
	island = DFSIslands(graph, start)
	while False in island.visited:
		count += 1
		start = island.visited.index(False)
		island.dfs(start)
	return count
	
import sys

V = int(sys.stdin.readline())
islands = Graph(V)

for line in sys.stdin:
	v, w = [int(n) for n in line.strip().split()]
	islands.addEdge(v, w)

print(count_islands(islands))
