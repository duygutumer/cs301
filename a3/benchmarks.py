import random
import time
random.seed(69)
vertices = 10 #change manually from here
class City:
  
  def __init__(self, name, bT): #bT is a list which holds train or bus or both
    self.name = name
    self.hasbus = bT[0] 
    self.hastrain = bT[1]
    self.hasboth = self.hasbus and self.hastrain
    self.distFromTrainToBus = False
    self.connections = {}

    if self.hasboth:
      self.distFromTrainToBus = random.randint(3, 10)
  
  def addConnection(self, dest, BT):
    distance = random.randint(50, 500)
    self.connections[dest] = (BT, distance)
    dest.connections[self] = (BT, distance)

def printGraph(graph):
  print("Printing graph with", len(graph), "nodes!")

  for i in range(len(graph)):
    print("Node", i, ":")
    if graph[i].hasboth:
      print("\t(Distance between stations =", graph[i].distFromTrainToBus, ")")
    if graph[i].hasbus:
      print("\tBus -> ", end="")
      for con, bt in graph[i].connections.items():
        if (bt[0] == "B"):
          print(con.name, "- (", bt[1], ") ", end="")
      print("")
    
    if (graph[i].hastrain):
      print("\tTrain -> ", end="")
      for con, bt in graph[i].connections.items():
        if (bt[0] == "T"):
          print(con.name, "- (", bt[1], ") ", end="")
      print("")

def isSuitable(A, B):
  if (A.name == B.name): return False
  if not ((A.hasbus and B.hasbus) or (A.hastrain and B.hastrain)): return False
  return True

def createGraph(num, addConn = 2):
  graph = []
  graph.append(City(0,[True, True])) #İstanbul has a bus and a train station
  # Create nodes
  for i in range(1, num): #i is a node name(0,1,2,...,num)
    b = random.randint(0, 1) == 1
    t = random.randint(0, 1) == 1
    if not (b or t): #since at least one of them must be
      if random.randint(0, 1) == 1: b = True
      else: t = True

    graph.append(City(i, [b,t]))

  for i in range(num):
    for j in range(addConn):
      randomChoice = random.randint(0, len(graph)-1)
      while not isSuitable(graph[i], graph[randomChoice]):
        randomChoice = random.randint(0, len(graph)-1)
      
      if random.randint(0,1) == 1:
        if (graph[i].hasbus and graph[randomChoice].hasbus):
          graph[i].addConnection(graph[randomChoice], "B")
        else:
          graph[i].addConnection(graph[randomChoice], "T")
      else:
        if (graph[i].hastrain and graph[randomChoice].hastrain):
          graph[i].addConnection(graph[randomChoice], "T")
        else:
          graph[i].addConnection(graph[randomChoice], "B")
  # Create connections
  return graph
