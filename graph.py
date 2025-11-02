
from collections import deque
import heapq



class graph:
  def __init__(self):
    self.graph = {}
  
  def add_vertex(self,vertex):
      if vertex  not in self.graph:
        self.graph[vertex] = []
        
  def add_edge(self,v1,v2):
    if v1 in self.graph and v2 in self.graph: # if both vertex are in graph ...then add edge otherwise send error infor
      self.graph[v1].append(v2)
      # if the graph is not directed then write this..in case of directed graph skip it
      self.graph[v2].append(v1)
    else:
      print(v1, "or " , v2 , "not in the graph kindly check it from graph")  
             
  def show(self):
    for i in self.graph:
      print(i,"  " ,self.graph[i]) 
      
  def delete_vertex(self,vertex):
    if vertex not in list(self.graph.keys()):
      print(vertex ,"  " , "not found")
      return
    
    for key in  list(self.graph.keys()):
      if vertex in self.graph[key]:
        self.graph[key].remove(vertex)
        
    del self.graph[vertex]
    
  def bfs(self, root):
    visited = []
    queue = []
    
    visited.append(root)
    queue.append(root)
    
    while queue:
      node = queue.pop(0)
      
      for child in self.graph[node]:
        if child not in visited:
           visited.append(child)
           queue.append(child)
           
    print(visited)  
    from collections import deque

  def bfs_level_order(graph, start):
      visited = set()
      queue = deque([start])
      level = 0  # track the level number
  
      while queue:
          level_size = len(queue)  # number of nodes in current level
          print(f"Level {level}:", end=" ")
  
          for _ in range(level_size):
              node = queue.popleft()
  
              if node not in visited:
                  visited.add(node)
                  print(node, end=" ")
  
                  for neighbor in graph[node]:
                      if neighbor not in visited:
                          queue.append(neighbor)
          
          print()  # move to next line after each level
          level += 1
          
  def dfs_iterative(self,start):
    visited =set()
    stack = []
    stack.append(start)
    
    while stack:
      node = stack.pop()
      if node not in visited:
        visited.add(node)
        print(node)
        for neighbour in reversed(self.graph[node]):
          if neighbour not in visited:
            stack.append(neighbour)
            
  def shortest_path(n,edges,src):
      adj = {}
      for i in range(n):          
        adj[i] = []
      
      
      for src,des,weight in edges:
        adj[src].append([des,weight])
        
      shortest = {}
      
      minHeap = [[0,src]]
      
      while minHeap:
        w1,n1 = heapq.heappop(minHeap)
        if n1 in shortest:
          continue
        for n2,w2 in adj[n]:
          if n2 not in shortest:
            heapq.heapush(minHeap,[w1+w2,n2])
            
      
      for i in range(n):
        if i not in shortest:
          shortest[i] = -1
          
      return shortest              
            
            
               
                
     
        
               
         
        
        
      
      

g = graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('D', 'C')

#===================================
g.show()
print()     
#====================================
g.delete_vertex('D')
print()
g.show()
#=====================================
print()
g.add_edge("1" , "2")
#========================================
g.bfs('B')


    