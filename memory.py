from operands import TYPES

class MemoryManager:
    def __init__(self):
        #const memory
        self.consM = Memory(0, 300, 500, 300, 1000, 300)
        #temp memory
        self.tempM = Memory(2000, 500, 3000, 500, 4000, 500)
        #global Memory
        self.globalM = Memory(5000, 300, 5600, 300, 6000, 300)
        #localMemory
        self.localM = Memory(9000, 300, 10000, 300, 11000, 300)


    def prepareMemory(self):
        self.memory = dict(self.consM.integerStack.items()+self.consM.doubleStack.items()+self.consM.booleanStack.items()
        +self.tempM.integerStack.items()+self.tempM.doubleStack.items()+self.tempM.booleanStack.items()
        +self.globalM.integerStack.items()+self.globalM.doubleStack.items()+self.globalM.booleanStack.items()
        +self.localM.integerStack.items()+self.localM.doubleStack.items()+self.localM.booleanStack.items())




    #sets the value into the memory space
    def writeOnMemory(self, memory, value):
        self.memory[int(memory)] = value

    #reads the value from the memory space
    def readFromMemory(self, memory):
        return self.memory[int(memory)]


    #clear local and temporal memory and constant memory
    def clearMemory(self):
        #temp memory
        self.tempM = Memory(2000, 500, 3000, 500, 4000, 500)
        #localMemory
        self.localM = Memory(9000, 300, 10000, 300, 11000, 300)
        #const memory
        self.consM = Memory(0, 300, 500, 300, 1000, 300)


class Memory:
    def __init__(self, intBeg, intSize, douBeg, douSize, booBeg, booSize):
        #parts of the memory
        self.integerStack = {}
        self.doubleStack = {}
        self.booleanStack = {}

        #memory segment initial position
        self.integerSegmentBeginning = intBeg
        self.doubleSegmentBeginning = douBeg
        self.booleanSegmentBeginning = booBeg

        #different values to simulate max memory
        self.integerMaxSize = self.integerSegmentBeginning + intSize
        self.doubleMaxSize = self.doubleSegmentBeginning + douSize
        self.booleanMaxSize = self.booleanSegmentBeginning + booSize

        #actual memory requested/used
        self.integerMemoryRequested = self.integerSegmentBeginning
        self.doubleMemoryRequested = self.doubleSegmentBeginning
        self.booleanMemoryRequested = self.booleanSegmentBeginning

    def requestMemoryOfType(self, memoryToRequest, type):
        if type == TYPES['int']:
            return self.requestIntMemory(memoryToRequest)
        elif type == TYPES['double']:
            return self.requestDoubleMemory(memoryToRequest)
        elif type == TYPES['boolean']:
            return self.requestBooleanMemory(memoryToRequest)
        else: #pointer required
            return self.requestPointerMemory(memoryToRequest)

    #sets the value into the memory space
    def writeOnMemory(self, memory, value, mType):
        if mType == TYPES['int']:
            self.integerStack[memory] = value
        elif mType == TYPES['double']:
            self.doubleStack[memory] = value
        elif mType == TYPES['boolean']:
            self.booleanStack[memory] = value

    #reads the value from the memory space
    def readFromMemory(self, memory, mType):
        if mType == TYPES['int']:
            return self.integerStack[memory]
        elif mType == TYPES['double']:
            return self.doubleStack[memory]
        elif mType == TYPES['boolean']:
            return self.booleanStack[memory]

    #different memory requests
    def requestIntMemory(self, memoryToRequest):
        memoryToReturn = self.integerMemoryRequested
        self.integerMemoryRequested += memoryToRequest
        if self.integerMemoryRequested > self.integerMaxSize:
            print "Memory stack overflow"
        self.integerStack[memoryToReturn] = None
        return memoryToReturn

    #different memory requests
    def requestDoubleMemory(self, memoryToRequest):
        memoryToReturn = self.doubleMemoryRequested
        self.doubleMemoryRequested += memoryToRequest
        if self.doubleMemoryRequested > self.doubleMaxSize:
            print "Memory stack overflow"
        self.doubleStack[memoryToReturn] = None
        return memoryToReturn

    #different memory requests
    def requestBooleanMemory(self, memoryToRequest):
        memoryToReturn = self.booleanMemoryRequested
        self.booleanMemoryRequested += memoryToRequest
        if self.booleanMemoryRequested > self.booleanMaxSize:
            print "Memory stack overflow"
        self.booleanStack[memoryToReturn] = None
        return memoryToReturn


memoryManager = MemoryManager()
