import PrioQ

#this will not get updated after the intital declaration
class edge:
    def __init__(self, location, distance):
        self.station = location
        self.dist = distance
    def __str__(self):
        return f"{self.station}||{self.dist}"
    def location(self):
        return self.station
    def distance(self):
        return float(self.dist)

def dijkstra(adjlist, startnode, predesessor, Weights):
    PQ = PrioQ.PriorityQ()
    PQ.push_back(0, startnode)
    while not PQ.empty():
        smallest = PQ.pop()
        Weights[smallest[1]] = smallest[0]
        if adjlist[smallest[1]] != None:
            for neighbor in adjlist[smallest[1]]:
                if(Weights[neighbor.location()] != -1):
                    pass
                elif(not PQ.exists(neighbor.location())):
                    distance = smallest[0] + neighbor.distance()
                    PQ.push_back(distance, neighbor.location())
                    predesessor[neighbor.location()] = smallest[1]
                elif((smallest[0] + neighbor.distance()) < PQ.get_value(neighbor.location())):
                    RELAX(smallest, neighbor, predesessor, PQ)
    return predesessor

            

def RELAX(curr, neighbor, predesessor, PQ):
    predesessor[neighbor.location()] = curr[1]
    PQ.decrease_key(curr[0] + neighbor.distance(), neighbor.location())
    



##
#main
##
Pathsandedges = {}
predesessor = {}
Weights = {}

file = open("paths.txt", "r")

data = file.read().split('\n')
for line in data:
    linesplit = line.split(' ')
    newedge = edge(linesplit[1], linesplit[2])
    if linesplit[0] in Pathsandedges:
        if Pathsandedges[linesplit[0]] == None:
            Pathsandedges[linesplit[0]] = [newedge]
        else:
            thislinelist = Pathsandedges[linesplit[0]]
            thislinelist.append(newedge)
        if linesplit[1] not in Weights:
            Weights[linesplit[1]] = -1
            predesessor[linesplit[1]] = ""
            Pathsandedges[linesplit[1]] = None
    else:
        Pathsandedges[linesplit[0]] = [newedge]
        if linesplit[0] not in Weights:
            Weights[linesplit[0]] = -1
            predesessor[linesplit[0]] = ""

file.close()
startingloc = input("what is your starting location?: ")

dijkstra(Pathsandedges, startingloc, predesessor, Weights)
print(predesessor)
print(Weights)