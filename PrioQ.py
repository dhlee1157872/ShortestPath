class PriorityQ:
    def __init__(self):
        self.PQ = []
        self.finddict = {}
    def push_back(self, weight, node):
        self.PQ.append([weight, node])
        self.finddict[node] = len(self.PQ) - 1
        self.BubbleUp(node)
    def BubbleUp(self, node):
        curr = self.finddict[node]
        if curr%2 == 0:
            parent = int(curr/2)-1
        else:
            parent = int(curr/2)
        while curr > 0:
            if(self.PQ[curr][0] < self.PQ[parent][0]):
                self.finddict[self.PQ[curr][1]] = parent
                self.finddict[self.PQ[parent][1]] = curr
                tmp = self.PQ[parent]
                self.PQ[parent] = self.PQ[curr]
                self.PQ[curr] = tmp
                curr = parent
                if curr%2 == 0:
                    parent = int(curr/2)-1
                else:
                    parent = int(curr/2)
            else:
                break
    def __str__(self):
        return f"{self.PQ}"
    def BubbleDown(self, node):
        curr = self.finddict[node]
        leftnode = curr*2 + 1
        rightnode = curr*2 + 2
        while rightnode < len(self.PQ):
            if(self.PQ[curr][0] > self.PQ[leftnode][0] or self.PQ[curr] > self.PQ[rightnode][0]):
                if(self.PQ[leftnode][0] > self.PQ[rightnode][0]):
                    self.finddict[self.PQ[curr][1]] = rightnode
                    self.finddict[self.PQ[rightnode][1]] = curr
                    tmp = self.PQ[rightnode]
                    self.PQ[rightnode] = self.PQ[curr]
                    self.PQ[curr] = tmp
                    curr = rightnode
                else:
                    self.finddict[self.PQ[curr][1]] = leftnode
                    self.finddict[self.PQ[leftnode][1]] = curr
                    tmp = self.PQ[leftnode]
                    self.PQ[leftnode] = self.PQ[curr]
                    self.PQ[curr] = tmp
                    curr = leftnode
                leftnode = curr*2 + 1
                rightnode = curr*2 + 2
            else:
                break
        if(leftnode < len(self.PQ)):
            if(self.PQ[curr][0] > self.PQ[leftnode][0]):
                    self.finddict[self.PQ[curr][1]] = leftnode
                    self.finddict[self.PQ[leftnode][1]] = curr
                    tmp = self.PQ[leftnode]
                    self.PQ[leftnode] = self.PQ[curr]
                    self.PQ[curr] = tmp
                    curr = leftnode
    def pop(self):
        value = self.PQ[0]
        del self.finddict[value[1]]
        if(len(self.PQ) > 1):
            self.PQ[0] = self.PQ[len(self.PQ) - 1]
            del self.PQ[len(self.PQ) - 1]
            self.finddict[self.PQ[0][1]] = 0
            self.BubbleDown(self.PQ[0][1])
        else:
            del self.PQ[0]
        return value
    def decrease_key(self, neweight, node):
        index = self.finddict[node]
        self.PQ[index][0] = neweight
        self.BubbleUp(node)
    def empty(self):
        if(len(self.PQ) > 0):
            return False
        return True
    def exists(self, node):
        if(self.finddict.get(node) == None):
            return False
        return True
    def get_value(self, node):
        index = self.finddict[node]
        return float(self.PQ[index][0])