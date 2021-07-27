from benchmarks import * 
Visited = []
infinity = float('inf')

def NaiveRecursion(graph, s, f, BT, depth = 0): #depth is for stop this recursion
  if s.name == f.name: #base case
    return 0
  
  if f in s.connections.keys(): #if there is one edge between s and f
    toAdd = 0 if s.connections[f][0] == BT else s.distFromTrainToBus
    return s.connections[f][1] + toAdd

  if depth >= vertices:
    return infinity

  result = infinity
  #Visited.append(s.name)
  for u, data in s.connections.items(): #for all neighbours of s
  #u->key data->value
      if data[0] == BT: #check bus or train station 
        recResult = NaiveRecursion(graph, u, f, BT, depth+1)
      else:
        travel = "B" if data[0] == "B" else "T"
        #print(s.name, travel)
        recResult = NaiveRecursion(graph, u, f, travel, depth+1)
      if recResult != infinity:
        toAdd = 0 if data[0] == BT else s.distFromTrainToBus #if they have different stations ex: Train -> Bus
        result = min(result, data[1] + toAdd + recResult) #we have to add this road from train to bus
     
  return result #just a node

def recursionTest(graph, s, BT):
  AddAll = 0
  for node in range(vertices): #for all nodes
    distance = NaiveRecursion(graph, s, graph[node], BT)
    print("0 ->", node,"with", distance, "km")
    AddAll += distance
  return AddAll

V = vertices #since we have 81 cities in Turkey we can write 81 (but now manually)
Visited = []
infinity = float('inf')

def Memoization(graph, s, BT):
  AddThem = 0
  sp = [[None] * V for i in range(V)]
  
  for i in range(V):
    for j in range(V):
      sp[i][j] = []
      for k in range(V):
        sp[i][j].append([None,None])
  
  for e in range(V): #number of possible edges
    for i in range(V): 
      for j in range(V):
        sp[i][j][e][0] = infinity #first make all of them infinity
        
        if e == 0 and i == j: #base case
          if i == s.name: #if starting node's name is same as i
            sp[i][j][e][1] = BT
          sp[i][j][e][0] = 0

        if e == 1 and graph[j] in graph[i].connections.keys(): #if num of edge is 1 and j is neighbour of i(starting point)
          specialCase = 0 #for the one edge case
          if i == s.name:
            if BT != graph[i].connections[graph[j]][0]: #if stations are different
              specialCase = s.distFromTrainToBus
        
          sp[i][j][e][0] = graph[i].connections[graph[j]][1] + specialCase #take distance
          sp[i][j][e][1] = graph[i].connections[graph[j]][0] #take station

        if e > 1:#if num of edge is bigger than 1
          for u, data in graph[i].connections.items():
            if sp[u.name][j][e - 1][0] != infinity:
              if data[0] == sp[u.name][j][e-1][1] or sp[u.name][j][e-1][1] == None: #is same station or there is no station do not add distance
                if (sp[i][j][e][0] >= data[1] + sp[u.name][j][e - 1][0]): #min(sp[i][j][e][0], data[1] + sp[u.name][j][e - 1][0])
                  sp[i][j][e][0] = data[1] + sp[u.name][j][e - 1][0] #take distance
                  sp[i][j][e][1] = sp[u.name][j][e - 1][1] #take station
                else:
                  sp[i][j][e][1] = sp[u.name][j][e-1][1]
                  
              else: #min(sp[i][j][e][0], data[1] + graph[i].distFromTrainToBus+ sp[u.name][j][e - 1][0])
                if (sp[i][j][e][0] >= data[1] + u.distFromTrainToBus + sp[u.name][j][e - 1][0]):
                  sp[i][j][e][0] = data[1] + u.distFromTrainToBus + sp[u.name][j][e - 1][0]
                  sp[i][j][e][1] = sp[u.name][j][e - 1][1]
                else:
                  sp[i][j][e][1] = sp[u.name][j][e-1][1]
      
      isAllNum = True #for all nodes, I found a number so I can stop
      for d in sp[s.name]:
        isNum = False #if there is a number then okay I found a number for this node
        for b in d:
          if b[0] != None and b[0] != infinity:
            #print(sp[s.name][f.name])
            isNum = True 
            break
        if not isNum:
          isAllNum = False
          break
      if isAllNum:
        for i in range(len(sp[s.name])):
          for j in range(len(sp[s.name][i])):
            if (sp[s.name][i][j][0] != None) and (sp[s.name][i][j][0] != infinity):
              print("0 ->", i,"with", sp[s.name][i][j][0], "km")
              AddThem += sp[s.name][i][j][0]
              break
        return AddThem
  for i in range(len(sp[s.name])):
    for j in range(len(sp[s.name][i])):
      if (sp[s.name][i][j][0] != None) and (sp[s.name][i][j][0] != infinity):
        print("0 ->", i,"with", sp[s.name][i][j][0], "km")
        AddThem += sp[s.name][i][j][0]
        break
  return AddThem

graph = createGraph(vertices)
printGraph(graph)

start = time.time()
allNodes = recursionTest(graph, graph[0], "B")
end = time.time()
print(allNodes)
print(end - start, "seconds")

start = time.time()
result = Memoization(graph,graph[0], "B")
end = time.time()
print(result)
print(end-start,"seconds")
