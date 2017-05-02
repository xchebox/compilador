from operands import TYPES

class MemoryManager:
    def __init__(self):
        #memory first and final local and temo memory
        self.tempIntI = 6000
        self.tempIntF = 6999
        self.tempDoubleI = 7000
        self.tempDoubleF = 7999
        self.tempBooleanI = 8000
        self.tempBooleanF = 8999
        self.localIntI = 9000
        self.localIntF = 9999
        self.localDoubleI = 10000
        self.localDoubleF = 10999
        self.localBooleanI = 11000
        self.localBooleanF = 11999

        #memory first and final global and constant memory
        self.globalIntI = 0
        self.globalIntF = 999
        self.globalDoubleI = 1000
        self.globalDoubleF = 1999
        self.globalBooleanI = 2000
        self.globalBooleanF = 2999
        self.constIntI = 3000
        self.constIntF = 3999
        self.constDoubleI = 4000
        self.constDoubleF = 4999
        self.constBooleanI = 5000
        self.constBooleanF = 5999

        #global Memory
        self.globalM = Memory(self.globalIntI, self.globalIntF, self.globalDoubleI, self.globalDoubleF, self.globalBooleanI, self.globalBooleanF)
        #const memory
        self.consM = Memory(self.constIntI, self.constIntF, self.constDoubleI, self.constDoubleF, self.constBooleanI, self.constBooleanF)
        #temp memory
        self.tempM = Memory(self.tempIntI, self.tempIntF, self.tempDoubleI, self.tempDoubleF, self.tempBooleanI, self.tempBooleanF)
        #localMemory
        self.localM = Memory(self.localIntI, self.localIntF, self.localDoubleI, self.localDoubleF, self.localBooleanI, self.localBooleanF)


    #sets the value into the memory space
    def writeOnMemory(self, memory, value):
        if memory >= self.constIntI and memory < self.constIntF:
            #print "int constant"
            self.consM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= self.constDoubleI and memory < self.constDoubleF:
            #print "double constant"
            self.consM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= self.globalBooleanI and memory < self.globalBooleanF:
            #print "boolean constant"
            self.consM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= self.tempIntI and memory < self.tempIntF:
            #print "int temp"
            self.tempM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= self.tempDoubleI and memory < self.tempDoubleF:
            #print "double temp"
            self.tempM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= self.tempBooleanI and memory < self.tempBooleanF:
            #print "boolean temp"
            self.tempM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= self.globalIntI and memory < self.globalIntF:
            #print "int global"
            self.globalM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= self.globalDoubleI and memory < self.globalDoubleF:
            #print "double global"
            self.globalM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= self.globalBooleanI and memory < self.globalBooleanF:
            #print "boolean global"
            self.globalM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= self.localIntI and memory < self.localIntF:
            #print "int local"
            self.localM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= self.localDoubleI and memory < self.localDoubleF:
            #print "double local"
            self.localM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= self.localBooleanI :
            #print "boolean local"
            self.localM.writeOnMemory(memory, value, TYPES['boolean'])

    #reads the value from the memory space
    def readFromMemory(self, memory):
        if memory >= self.constIntI and memory < self.constIntF:
            #print "int constant"
            return self.consM.readFromMemory(memory, TYPES['int'])
        if memory >= self.constDoubleI and memory < self.constDoubleF:
            #print "double constant"
            return self.consM.readFromMemory(memory, TYPES['double'])
        if memory >= self.constBooleanI and memory < self.constBooleanF:
            #print "boolean constant"
            return self.consM.readFromMemory(memory, TYPES['boolean'])
        if memory >= self.tempIntI and memory < self.tempIntF:
            #print "int temp"
            return self.tempM.readFromMemory(memory, TYPES['int'])
        if memory >= self.tempDoubleI and memory < self.tempDoubleF:
            #print "double temp"
            return self.tempM.readFromMemory(memory, TYPES['double'])
        if memory >= self.tempBooleanI and memory < self.tempBooleanF:
            #print "boolean temp"
            return self.tempM.readFromMemory(memory, TYPES['boolean'])
        if memory >= self.globalIntI and memory < self.globalIntF:
            #print "int global"
            return self.globalM.readFromMemory(memory, TYPES['int'])
        if memory >= self.globalDoubleI and memory < self.globalDoubleF:
            #print "double global"
            return self.globalM.readFromMemory(memory, TYPES['double'])
        if memory >= self.globalBooleanI and memory < self.globalBooleanF:
            #print "boolean global"
            return self.globalM.readFromMemory(memory, TYPES['boolean'])
        if memory >= self.localIntI and memory < self.localIntF:
            #print "int local"
            return self.localM.readFromMemory(memory, TYPES['int'])
        if memory >= self.localDoubleI and memory < self.localDoubleF:
            #print "double local"
            return self.localM.readFromMemory(memory, TYPES['double'])
        if memory >= self.localBooleanI :
            #print "boolean local"
            return self.localM.readFromMemory(memory, TYPES['boolean'])
        return None


    #clear local and temporal memory and constant memory
    def clearMemory(self):
        #temp memory
        self.tempM = Memory(self.tempIntI, self.tempIntF, self.tempDoubleI, self.tempDoubleF, self.tempBooleanI, self.tempBooleanF)
        #localMemory
        self.localM = Memory(self.localIntI, self.localIntF, self.localDoubleI, self.localDoubleF, self.localBooleanI, self.localBooleanF)
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
        self.integerMaxSize = intSize
        self.doubleMaxSize = douSize
        self.booleanMaxSize = booSize

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
