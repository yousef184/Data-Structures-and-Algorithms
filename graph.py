from collections import deque

class graph:
    def __init__(self):
        self.dict = {}
        self.routes = []
        pass

    def update_dict(self):
        for route in self.routes:
            if route[0] in self.dict and ([route[1],route[2]] not in self.dict[route[0]]):
                self.dict[route[0]].append([route[1],route[2]])
                if route[1] in self.dict and ([route[0],route[2]] not in self.dict[route[1]]):
                    self.dict[route[1]].append([route[0],route[2]])
                else:
                    self.dict[route[1]]= [[route[0],route[2]]]
            else:
                self.dict[route[0]]= [[route[1],route[2]]]
                if route[1] in self.dict and ([route[0],route[2]] not in self.dict[route[1]]):
                    self.dict[route[1]].append([route[0],route[2]])
                else:    
                    self.dict[route[1]]= [[route[0],route[2]]]

    def print(self):
        print(self.dict)

    def insert(self, source, destination, weight):
        temp = (source, destination, weight)
        self.routes.append(temp)
        self.update_dict()

    def route(self,source,destination):
        unvisited = list(self.dict.keys())
        visited= []
        shortestDistance = {}
        for key in unvisited:
            shortestDistance[key] = [1000,None]
        shortestDistance[source] = 0
        visited.append(source)
        currentNode = source
        currentDist = 0
        while len(visited)<len(self.dict.keys()):
            min = [None,1000]
            for items in self.dict[currentNode]:
                if items[0] in unvisited and items[1]+currentDist < shortestDistance[items[0]][0]:
                    shortestDistance[items[0]][0] = items[1]+currentDist
                    shortestDistance[items[0]][1] = currentNode
                    if items[1] < min[1]:
                        min = items
            visited.append(currentNode)
            unvisited.remove(currentNode)
            currentNode = min[0]
            currentDist += min[1]
        return shortestDistance[destination][0], self.make_route(shortestDistance,source,destination) 
    
    def make_route(self,shortestDistance,source,destination):
        queue = deque()
        while destination != source:
            for key in self.dict.keys():
                if key == destination:
                    queue.appendleft(destination)
                    destination = shortestDistance[key][1]
        queue.appendleft(source)
        return queue



myGraph = graph()
myGraph.insert('a','b',6)
myGraph.insert('a','d',1)
myGraph.insert('b','d',2)
myGraph.insert('b','e',2)
myGraph.insert('b','c',5)
myGraph.insert('e','d',1)
myGraph.insert('e','c',5)

print(myGraph.route('a','c'))
# myGraph.print()