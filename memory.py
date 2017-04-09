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


        #different memory requests
        def requestIntMemory(self, memoryToRequest):
            memoryToReturn = 0
            self.integerMemoryRequested += memoryToRequest
            if self.integerMemoryRequested > integerMaxSize:
                print "Memory stack overflow"
            return memoryToReturn

        #different memory requests
        def requestDoubleMemory(self, memoryToRequest):
            memoryToReturn = 0
            self.doubleMemoryRequested += memoryToRequest
            if self.doubleMemoryRequested > doubleMaxSize:
                print "Memory stack overflow"
            return memoryToReturn

        #different memory requests
        def requestIntMemory(self, memoryToRequest):
            memoryToReturn = 0
            self.booleanMemoryRequested += memoryToRequest
            if self.booleanMemoryRequested > booleanMaxSize:
                print "Memory stack overflow"
            return memoryToReturn

        #different memory requests
        def requestIntMemory(self, memoryToRequest):
            memoryToReturn = 0
            self.pointerMemoryRequested += memoryToRequest
            if self.pointerMemoryRequested > pointerMaxSize:
                print "Memory stack overflow"
            return memoryToReturn
