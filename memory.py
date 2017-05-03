from operands import TYPES

class MemoryManager:
    def __init__(self, intTempSize = None, doubleTempSize = None, booleanTempSize = None, intLocalSize = None, doubleLocalSize = None, booleanLocalSize = None,
     intTempOff = None, doubleTempOff = None, booleanTempOff = None, intLocalOff = None, doubleLocalOff = None, booleanLocalOff = None):
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

        self.intTempOff = 0
        self.doubleTempOff = 0
        self.booleanTempOff = 0
        self.intLocalOff = 0
        self.doubleLocalOff = 0
        self.booleanLocalOff = 0

        #is called with offset. Need to reallocate memory
        if not intTempOff is None:
            self.tempIntI += intTempOff
            self.intTempOff = intTempOff
        if not doubleTempOff is None:
            self.tempDoubleI += doubleTempOff
            self.doubleTempOff = doubleTempOff
        if not booleanTempOff is None:
            self.tempBooleanI += booleanTempOff
            self.booleanTempOff = booleanTempOff
        if not intLocalOff is None:
            self.localIntI += intLocalOff
            self.intLocalOff = intLocalOff
        if not doubleLocalOff is None:
            self.localDoubleI += doubleLocalOff
            self.doubleLocalOff = doubleLocalOff
        if not booleanLocalOff is None:
            self.localBooleanI += booleanLocalOff
            self.booleanLocalOff = booleanLocalOff

        # if is called as memory instance then you only request the neccesary memory
        if not intTempSize is None:
            self.tempIntF = self.tempIntI + intTempSize
        if not doubleTempSize is None:
            self.tempDoubleF = self.tempDoubleI + doubleTempSize
        if not booleanTempSize is None:
            self.tempBooleanF = self.tempBooleanI + booleanTempSize
        if not intLocalSize is None:
            self.localIntF = self.localIntI + intLocalSize
        if not doubleLocalSize is None:
            self.localDoubleF = self.localDoubleI + doubleLocalSize
        if not booleanLocalSize is None:
            self.localBooleanF = self.localBooleanI + booleanLocalSize

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

        # if called as instance memory does not request global or constant memory
        if not intTempSize is None:
            #global Memory
            self.globalM = Memory(0, 0, 0, 0, 0, 0)
            #const memory
            self.consM = Memory(0, 0, 0, 0, 0, 0)
        else:
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
        memory = int(memory)
        if memory >= self.constIntI and memory < self.constIntF:
            #print "int constant"
            self.consM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= self.constDoubleI and memory < self.constDoubleF:
            #print "double constant"
            self.consM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= self.globalBooleanI and memory < self.globalBooleanF:
            #print "boolean constant"
            self.consM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= self.tempIntI - self.intTempOff and memory < self.tempIntF - self.intTempOff:
            #print "int temp"
            self.tempM.writeOnMemory(memory - self.intTempOff, value, TYPES['int'])
        if memory >= self.tempDoubleI - self.doubleTempOff and memory < self.tempDoubleF - self.doubleTempOff:
            #print "double temp"
            self.tempM.writeOnMemory(memory - self.doubleTempOff, value, TYPES['double'])
        if memory >= self.tempBooleanI - self.booleanTempOff and memory < self.tempBooleanF - self.booleanTempOff:
            #print "boolean temp"
            self.tempM.writeOnMemory(memory - self.booleanTempOff, value, TYPES['boolean'])
        if memory >= self.globalIntI and memory < self.globalIntF:
            #print "int global"
            self.globalM.writeOnMemory(memory, value, TYPES['int'])
        if memory >= self.globalDoubleI and memory < self.globalDoubleF:
            #print "double global"
            self.globalM.writeOnMemory(memory, value, TYPES['double'])
        if memory >= self.globalBooleanI and memory < self.globalBooleanF:
            #print "boolean global"
            self.globalM.writeOnMemory(memory, value, TYPES['boolean'])
        if memory >= self.localIntI - self.intLocalOff and memory < self.localIntF - self.intLocalOff:
            #print "int local"
            #print value
            self.localM.writeOnMemory(memory - self.intLocalOff, value, TYPES['int'])
        if memory >= self.localDoubleI - self.doubleLocalOff and memory < self.localDoubleF - self.doubleLocalOff:
            #print "double local"
            self.localM.writeOnMemory(memory - self.doubleLocalOff, value, TYPES['double'])
        if memory >= self.localBooleanI - self.booleanLocalOff :
            #print "boolean local"
            self.localM.writeOnMemory(memory - self.booleanLocalOff, value, TYPES['boolean'])

    #reads the value from the memory space
    def readFromMemory(self, memory):
        memory = int(memory)
        if memory >= self.constIntI and memory < self.constIntF:
            #print "int constant"
            return self.consM.readFromMemory(memory, TYPES['int'])
        if memory >= self.constDoubleI and memory < self.constDoubleF:
            #print "double constant"
            return self.consM.readFromMemory(memory, TYPES['double'])
        if memory >= self.constBooleanI and memory < self.constBooleanF:
            #print "boolean constant"
            return self.consM.readFromMemory(memory, TYPES['boolean'])
        if memory >= self.tempIntI - self.intTempOff and memory < self.tempIntF - self.intTempOff:
            #print "int temp"
            return self.tempM.readFromMemory(memory - self.intTempOff, TYPES['int'])
        if memory >= self.tempDoubleI - self.doubleTempOff and memory < self.tempDoubleF - self.doubleTempOff:
            #print "double temp"
            return self.tempM.readFromMemory(memory - self.doubleTempOff, TYPES['double'])
        if memory >= self.tempBooleanI - self.booleanTempOff and memory < self.tempBooleanF - self.booleanTempOff:
            #print "boolean temp"
            return self.tempM.readFromMemory(memory - self.booleanTempOff, TYPES['boolean'])
        if memory >= self.globalIntI and memory < self.globalIntF:
            #print "int global"
            return self.globalM.readFromMemory(memory, TYPES['int'])
        if memory >= self.globalDoubleI and memory < self.globalDoubleF:
            #print "double global"
            return self.globalM.readFromMemory(memory, TYPES['double'])
        if memory >= self.globalBooleanI and memory < self.globalBooleanF:
            #print "boolean global"
            return self.globalM.readFromMemory(memory, TYPES['boolean'])
        if memory >= self.localIntI - self.intLocalOff and memory < self.localIntF - self.intLocalOff:
            #print memory >= self.localIntI and memory < self.localIntF
            #print "int local"
            return self.localM.readFromMemory(memory - self.intLocalOff, TYPES['int'])
        if memory >= self.localDoubleI - self.doubleLocalOff and memory < self.localDoubleF - self.doubleLocalOff:
            #print "double local"
            return self.localM.readFromMemory(memory - self.doubleLocalOff , TYPES['double'])
        if memory >= self.localBooleanI - self.booleanLocalOff:
            #print "boolean local"
            return self.localM.readFromMemory(memory - self.booleanLocalOff, TYPES['boolean'])
        return None


    #clear local and temporal memory and constant memory
    def clearMemory(self):
        #temp memory
        self.tempM = Memory(self.tempIntI, self.tempIntF, self.tempDoubleI, self.tempDoubleF, self.tempBooleanI, self.tempBooleanF)
        #localMemory
        self.localM = Memory(self.localIntI, self.localIntF, self.localDoubleI, self.localDoubleF, self.localBooleanI, self.localBooleanF)
        #const memory
        #elf.consM = Memory(0, 300, 500, 300, 1000, 300)


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

class MemoryCounter:
    def __init__(self):
        self.tempInt = 0
        self.tempDouble = 0
        self.tempBoolean = 0
        self.localInt = 0
        self.localDouble = 0
        self.localBoolean = 0

memoryManager = MemoryManager()
