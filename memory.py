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


    #sets the value into the memory space
    def writeOnMemory(self, memory, value):
        if memory >= 0 and memory < 500:
            #print "int constant"
            self.consM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= 500 and memory < 1000:
            #print "double constant"
            self.consM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= 1000 and memory < 2000:
            #print "boolean constant"
            self.consM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= 2000 and memory < 3000:
            #print "int temp"
            self.tempM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= 3000 and memory < 4000:
            #print "double temp"
            self.tempM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= 4000 and memory < 5000:
            #print "boolean temp"
            self.tempM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= 5000 and memory < 5600:
            #print "int global"
            self.globalM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= 5600 and memory < 6000:
            #print "double global"
            self.globalM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= 6000 and memory < 9000:
            #print "boolean global"
            self.globalM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= 9000 and memory < 10000:
            #print "int local"
            self.localM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= 10000 and memory < 11000:
            #print "double local"
            self.localM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= 11000 :
            #print "boolean local"
            self.localM.writeOnMemory(memory, value, TYPES['boolean'])

    #reads the value from the memory space
    def readFromMemory(self, memory):
        if memory >= 0 and memory < 500:
            #print "int constant"
            return self.consM.readFromMemory(memory, TYPES['int'])
        if memory >= 500 and memory < 1000:
            #print "double constant"
            return self.consM.readFromMemory(memory, TYPES['double'])
        if memory >= 1000 and memory < 2000:
            #print "boolean constant"
            return self.consM.readFromMemory(memory, TYPES['boolean'])
        if memory >= 2000 and memory < 3000:
            #print "int temp"
            return self.tempM.readFromMemory(memory, TYPES['int'])
        if memory >= 3000 and memory < 4000:
            #print "double temp"
            return self.tempM.readFromMemory(memory, TYPES['double'])
        if memory >= 4000 and memory < 5000:
            #print "boolean temp"
            return self.tempM.readFromMemory(memory, TYPES['boolean'])
        if memory >= 5000 and memory < 5600:
            #print "int global"
            return self.globalM.readFromMemory(memory, TYPES['int'])
        if memory >= 5600 and memory < 6000:
            #print "double global"
            return self.globalM.readFromMemory(memory, TYPES['double'])
        if memory >= 6000 and memory < 9000:
            #print "boolean global"
            return self.globalM.readFromMemory(memory, TYPES['boolean'])
        if memory >= 9000 and memory < 10000:
            #print "int local"
            return self.localM.readFromMemory(memory, TYPES['int'])
        if memory >= 10000 and memory < 11000:
            #print "double local"
            return self.localM.readFromMemory(memory, TYPES['double'])
        if memory >= 11000 :
            #print "boolean local"
            return self.localM.readFromMemory(memory, TYPES['boolean'])
        return None


    #clear local and temporal memory and constant memory
    def clearMemory(self):
        #temp memory
        self.tempM = Memory(2000, 500, 3000, 500, 4000, 500)
        #localMemory
        self.localM = Memory(9000, 300, 10000, 300, 11000, 300)
        #const memory
        #elf.consM = Memory(0, 300, 500, 300, 1000, 300) TODO uncomment this and manage contant memory


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
            if not memory in self.integerStack:
                return None
            return self.integerStack[memory]
        elif mType == TYPES['double']:
            if not memory in self.doubleStack:
                return None
            return self.doubleStack[memory]
        elif mType == TYPES['boolean']:
            if not memory in self.booleanStack:
                return None
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
