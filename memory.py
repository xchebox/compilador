from operands import TYPES

class MemoryManager:
    def __init__(self):

        #memory segment initial position
        self.integerSegmentBeginning = 1000
        self.doubleSegmentBeginning = 5300
        self.booleanSegmentBeginning = 9273
        self.pointerSegmentBeginning = 13004

        #different values to simulate max memory
        self.integerMaxSize = self.integerSegmentBeginning + 1000
        self.doubleMaxSize = self.doubleSegmentBeginning + 1000
        self.booleanMaxSize = self.booleanSegmentBeginning + 1000
        self.pointerMaxSize = self.pointerSegmentBeginning + 1000

        #actual memory requested/used
        self.integerMemoryRequested = self.integerSegmentBeginning
        self.doubleMemoryRequested = self.doubleSegmentBeginning
        self.booleanMemoryRequested = self.booleanSegmentBeginning
        self.pointerMemoryRequested = self.pointerSegmentBeginning

        #parts of the memory
        self.integerStack = {}
        self.doubleStack = {}
        self.booleanStack = {}
        self.pointerStack = {}


    def requestMemoryOfType(self, memoryToRequest, type):
        if type == TYPES['int']:
            return self.requestIntMemory(memoryToRequest)
        elif type == TYPES['double']:
            return self.requestDoubleMemory(memoryToRequest)
        elif type == TYPES['boolean']:
            return self.requestBooleanMemory(memoryToRequest)
        else: #pointer required
            return self.requestPointerMemory(memoryToRequest)

    #different memory requests
    def requestIntMemory(self, memoryToRequest):
        memoryToReturn = self.integerMemoryRequested
        self.integerMemoryRequested += memoryToRequest
        if self.integerMemoryRequested > self.integerMaxSize:
            print "Memory stack overflow"
        return memoryToReturn

    #different memory requests
    def requestDoubleMemory(self, memoryToRequest):
        memoryToReturn = self.doubleMemoryRequested
        self.doubleMemoryRequested += memoryToRequest
        if self.doubleMemoryRequested > self.doubleMaxSize:
            print "Memory stack overflow"
        return memoryToReturn

    #different memory requests
    def requestBooleanMemory(self, memoryToRequest):
        memoryToReturn = self.booleanMemoryRequested
        self.booleanMemoryRequested += memoryToRequest
        if self.booleanMemoryRequested > self.booleanMaxSize:
            print "Memory stack overflow"
        return memoryToReturn

    #different memory requests
    def requestPointerMemory(self, memoryToRequest):
        memoryToReturn = self.pointerMemoryRequested
        self.pointerMemoryRequested += memoryToRequest
        if self.pointerMemoryRequested > self.pointerMaxSize:
            print "Memory stack overflow"
        return memoryToReturn
