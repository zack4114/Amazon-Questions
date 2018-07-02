# Breadth First Search or BFS for a Graph
# Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree 
# (See method 2 of this post). The only catch here is, unlike trees, graphs may contain cycles, so we may
#  come to the same node again. To avoid processing a node more than once, we use a boolean visited array. 
#  For simplicity, it is assumed that all vertices are reachable from the starting vertex.
# For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for 
# all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will 
# be processed again and it will become a non-terminating process. A Breadth First Traversal of the following graph 
# is 2, 0, 3, 1.

import collections
class Graph(object):
	def __init__(self):
		self.graph = collections.defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self,x):
		visited = [False]*len(self.graph)
		q = []
		q.insert(0,x)
		visited[x] = True

		while(len(q) is not 0):
			x = q.pop()
			print(x,end = " ")
			for i in self.graph[x]:
				if visited[i] is False:
					q.insert(0,i)
					visited[i] = True
		print()

	def DFS(self,x):
		stack = []
		visited = [False]*len(self.graph)
		stack.append(x)
		visited[x] = True
		while(len(stack) is not 0):

			x = stack.pop()
			print(x,end=" ")
			for i in self.graph[x]:
				if visited[i] is False:
					stack.append(i)
					visited[i] = True
		print()


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.BFS(2)
g.DFS(2)

