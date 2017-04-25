#from memory import MemoryManager
from quadruple import Quadruple
from operators import operators
from memory import memoryManager

class VirtualMachine:

    def __init__(self):
        #instructions/quadruples
        self.instructions = {}
        #program counter. To know current Quadruple
        self.pc = 0

    def loadProgram(self):
        file = open("./out/quadruple.cp", "r")

        ic = 0
        for line in file:
            q = line.split(',')
            q[3] = q[3].rstrip('\n')
            self.instructions[ic] = Quadruple(q[0], q[1], q[2], q[3])
            ic += 1

    def run(self):
        while  self.instructions[self.pc].operator != operators['end']:
            instruction = self.instructions[self.pc]
            if instruction.operator == operators['+']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand)+
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['-']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand)-
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['*']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand)*
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['/']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand)/
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['==']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand) ==
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['=']:
                print '='
            elif instruction.operator == operators['<']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand)<
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['>']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand)>
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['&']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand) and
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

            elif instruction.operator == operators['|']:
                if memoryManager.readFromMemory(instruction.firstOperand) is None or memoryManager.readFromMemory(instruction.secondOperand) is None:
                    return 'Error, variable used but not assigned'

                memoryManager.writeOnMemory(
                instruction.result,
                memoryManager.readFromMemory(instruction.firstOperand) or
                memoryManager.readFromMemory(instruction.secondOperand)
                )
                print memoryManager.readFromMemory(instruction.result)

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
