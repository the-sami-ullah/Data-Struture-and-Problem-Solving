

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
g.show()
print()     
g.delete_vertex('D')
print()
g.show()
print()
g.add_edge("1" , "2")

    