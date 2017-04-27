#from memory import MemoryManager
from quadruple import Quadruple
from operators import operators
from memory import memoryManager as gMemory, MemoryManager

class VirtualMachine:

    def __init__(self):
        #instructions/quadruples
        self.instructions = {}
        #program counter. To know current Quadruple
        self.pc = 0
        self.pointerStack = []
        self.memoryMap = {}
        self.mStack = [] #memory stack
        print gMemory.globalM.integerStack


    def readFromMemory(self, memory):
        #print memory
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            return gMemory.readFromMemory(memory)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            return gMemory.readFromMemory(memory)
        else :
            return self.mStack[len(self.mStack) - 1].readFromMemory(memory)

    def readFromPreviousMemory(self, memory):
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            return gMemory.readFromMemory(memory)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            return gMemory.readFromMemory(memory)
        else :
            return self.mStack[len(self.mStack) - 2].readFromMemory(memory)

    def writeOnMemory(self, memory, value):
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            gMemory.writeOnMemory(memory, value)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            gMemory.writeOnMemory(memory, value)
        else:
            self.mStack[len(self.mStack) - 1].writeOnMemory(memory, value)

    def loadMemory(self, functionName):
        self.mStack.append(MemoryManager())

    def loadProgram(self):
        file = open("./out/quadruple.cp", "r")

        memory_map_header = next(file).rstrip('\n')
        tStack  = list(memory_map_header.split('.'))
        while len(tStack) > 0:
            v = tStack.pop()
            k = tStack.pop()
            self.memoryMap[k] = list(v.split(','))
        #for k in self.memoryMap:
        #    print "%s = %s"%(k, self.memoryMap[k])



        ic = 0
        for line in file:
            q = line.split(',')
            q[3] = q[3].rstrip('\n')
            self.instructions[ic] = Quadruple(q[0], q[1], q[2], q[3])
            ic += 1

    def run(self):
        self.loadMemory('main')#loads main memory segment

        while  self.instructions[self.pc].operator != operators['end']:
            print operators.keys()[operators.values().index(self.instructions[self.pc].operator)]
            instruction = self.instructions[self.pc]
            if instruction.operator == operators['+']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)+
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['-']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)-
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['*']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)*
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['/']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)/
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['==']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand) ==
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['=']:
                if self.readFromMemory(instruction.firstOperand) is None:
                    return 'Error, variable used but not assigned'
                self.writeOnMemory(instruction.result,
                self.readFromMemory(instruction.firstOperand))

            elif instruction.operator == operators['<']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)<
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['>']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)>
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['&']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand) and
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['|']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand) or
                self.readFromMemory(instruction.secondOperand)
                )

            elif instruction.operator == operators['goto']:
                self.pc = int(instruction.result) - 1 # -1 because after this code it sums 1 before ending the cycle


            elif instruction.operator == operators['gotoF']:

                if self.readFromMemory(instruction.firstOperand) is None:
                    return 'Error, variable used but not assigned'
                if not self.readFromMemory(instruction.firstOperand):
                    self.pc = int(instruction.result) - 1

            elif instruction.operator == operators['gotoT']:

                if self.readFromMemory(instruction.firstOperand) is None:
                    return 'Error, variable used but not assigned'
                if self.readFromMemory(instruction.firstOperand):
                    self.pc = int(instruction.result) - 1

            elif instruction.operator == operators['return']:

                if self.readFromMemory(instruction.firstOperand) is None:
                    return 'Error, variable used but not assigned'
                self.writeOnMemory(instruction.result,
                self.readFromMemory(instruction.firstOperand))
                #retrieve last pointer to jump back where function was called
                self.pc = int(self.pointerStack.pop())
                #release memory
                self.mStack.pop()

            elif instruction.operator == operators['era']:

                #loads new memory to stack
                self.loadMemory(instruction.firstOperand)

            elif instruction.operator == operators['goSub']:
                #adds pointer to stack to know how to jump back after return
                self.pointerStack.append(self.pc)
                self.pc = int(instruction.result) - 1

            elif instruction.operator == operators['param']:

                # we use previous memoty because we are adding info from last memory segment before change context
                if self.readFromPreviousMemory(instruction.firstOperand) is None:
                    return 'Error, variable used but not assigned'
                self.writeOnMemory(instruction.result,
                self.readFromPreviousMemory(instruction.firstOperand))

            self.pc += 1

        return 'Process finished successful'
