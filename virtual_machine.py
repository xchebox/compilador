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
        self.memoryMap = {}
        self.mStack = [] #memory stack


    def readFromMemory(self, memory):
        if memory >= 5000 and memory < 9000: #global memory
            return gMemory.readFromMemory(memory)
        else :
            return self.mStack[len(self.mStack) - 1].readFromMemory(memory)

    def writeOnMemory(self, memory, value):
        if memory >= 5000 and memory < 9000: #global memory
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
            instruction = self.instructions[self.pc]
            if instruction.operator == operators['+']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)+
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['-']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)-
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['*']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)*
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['/']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)/
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['==']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand) ==
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['=']:
                print '='
            elif instruction.operator == operators['<']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)<
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['>']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand)>
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['&']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand) and
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['|']:
                if self.readFromMemory(instruction.firstOperand) is None or self.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(
                instruction.result,
                self.readFromMemory(instruction.firstOperand) or
                self.readFromMemory(instruction.secondOperand)
                )
                print self.readFromMemory(instruction.result)

            elif instruction.operator == operators['goto']:
                self.pc = int(instruction.result) - 1


            elif instruction.operator == operators['gotoF']:
                print 'gotoF'
            elif instruction.operator == operators['gotoT']:
                print 'gotoT'
            elif instruction.operator == operators['return']:
                print 'return'
            elif instruction.operator == operators['era']:
                print 'era'
            elif instruction.operator == operators['goSub']:
                print 'goSub'
            elif instruction.operator == operators['param']:
                print 'param'
            self.pc += 1

        return 'Process finished successful'
