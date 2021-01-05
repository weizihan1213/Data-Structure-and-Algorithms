class Graph:
  def __init__(self):
    self.numberOfNodes = 0
    self.adjacentList = {}

  def addVertex(self, node):
      self.adjacentList[node] = []
      self.numberOfNodes += 1
      return


  def addEdge(self, node1, node2):
    if node1 not in self.adjacentList:
      print(f'Node {node1} has not been added into the Graph')
      return
    elif node2 not in self.adjacentList:
      print(f'Node {node2} has not been added into the Graph')
      return
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)
    return 


  def showConnection(self):
    for key, value in self.adjacentList.items():
      print (f'{key} -> {value}')


myGph1 = Graph()
myGph1.addVertex(0)
myGph1.addVertex(1)
myGph1.addVertex(2)
myGph1.addVertex(3)
myGph1.addVertex(4)
myGph1.addVertex(5)
myGph1.addVertex(6)
myGph1.addEdge(0, 1)
myGph1.addEdge(0, 2)
myGph1.addEdge(1, 2)
myGph1.addEdge(3, 1)
myGph1.addEdge(3, 4)
myGph1.addEdge(2, 4)
myGph1.addEdge(4, 5)
myGph1.addEdge(5, 6)
myGph1.addEdge(8, 1)
myGph1.showConnection()