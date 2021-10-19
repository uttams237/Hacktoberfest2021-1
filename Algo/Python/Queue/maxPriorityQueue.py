# maxPriorityQueue

# 1. getSize -
# Return the size of priority queue i.e. number of elements present in the priority queue.
# 2. isEmpty -
# Check if priority queue is empty or not. Return true or false accordingly.
# 3. insert -
# Given an element, insert that element in the priority queue at the correct position.
# 4. getMax -
# Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.
# 5. removeMax -
# Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty


class pqNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pqArr = []

    def isEmpty(self):
        return self.getSize() == 0
        # Implement the isEmpty() function here

    def getSize(self):
        return len(self.pqArr)
        # Implement the getSize() function here

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pqArr[0].value
        # Implement the getMax() function here

    def __percolateUp(self, item):
        childIndex = self.getSize()-1
        while True:
            parentIndex = (childIndex-1)//2
            if self.pqArr[childIndex].priority > self.pqArr[parentIndex].priority:
                self.pqArr[childIndex], self.pqArr[parentIndex] = self.pqArr[parentIndex], self.pqArr[childIndex]
                childIndex = parentIndex
                if childIndex == 0:
                    break
            else:
                break

    def insert(self, ele, priority):
        item = pqNode(ele, priority)
        self.pqArr.append(item)
        self.__percolateUp(item)
        # Implement the insert() function here

    def __percolateDown(self):
        self.pqArr[0] = self.pqArr.pop()
        parentIndex = 0
        while True:
            lcIndex, rcIndex = (2*parentIndex)+1, (2*parentIndex)+2
            if lcIndex > self.getSize()-1:
                break
            if rcIndex > self.getSize()-1:
                if self.pqArr[parentIndex].priority < self.pqArr[lcIndex].priority:
                    self.pqArr[parentIndex], self.pqArr[lcIndex] = self.pqArr[lcIndex], self.pqArr[parentIndex]
                    parentIndex = lcIndex
                break
                # else:
                #     break
            if self.pqArr[lcIndex].priority>self.pqArr[rcIndex].priority:
                bigPriorityIndex=lcIndex
            else:
                bigPriorityIndex=rcIndex

            if self.pqArr[parentIndex].priority<self.pqArr[bigPriorityIndex].priority:
                self.pqArr[parentIndex],self.pqArr[bigPriorityIndex]=self.pqArr[bigPriorityIndex],self.pqArr[parentIndex]
                parentIndex=bigPriorityIndex
            else:
                break



    def removeMax(self):
        if self.isEmpty():
            return None
        if self.getSize()==1:
            return self.pqArr.pop().value
        ans = self.pqArr[0].value
        self.__percolateDown()
        return ans
        # Implement the removeMax() function here


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1
