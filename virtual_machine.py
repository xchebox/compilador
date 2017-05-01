#from memory import MemoryManager
from quadruple import Quadruple
from operators import operators
from memory import memoryManager as gMemory, MemoryManager
import turtle

class VirtualMachine:

    def __init__(self):
        #instructions/quadruples
        self.instructions = {}
        #program counter. To know current Quadruple
        self.pc = 0
        self.tempMemory = MemoryManager()
        self.pointerStack = []
        self.memoryMap = {}
        self.mStack = [] #memory stack
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()


    def readFromMemory(self, memory):
        #print memory
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            return gMemory.readFromMemory(memory)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            return gMemory.readFromMemory(memory)
        else :
            return self.mStack[len(self.mStack) - 1].readFromMemory(memory)

    def writeOnMemory(self, memory, value):
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            gMemory.writeOnMemory(memory, value)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            gMemory.writeOnMemory(memory, value)
        else:
            self.mStack[len(self.mStack) - 1].writeOnMemory(memory, value)

    def writeOnPreviousMemory(self, memory, value):
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            gMemory.writeOnMemory(memory, value)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            gMemory.writeOnMemory(memory, value)
        else:
            self.mStack[len(self.mStack) - 2].writeOnMemory(memory, value)

    def writeOnNewMemory(self, memory, value):
        memory = int(memory)
        if memory >= 5000 and memory < 9000: #global memory
            gMemory.writeOnMemory(memory, value)
        elif memory >= 0 and memory < 2000: #constant memory TODO delete this to manage constants
            gMemory.writeOnMemory(memory, value)
        else:
            self.tempMemory.writeOnMemory(memory, value)

    def requestMemory(self, functionName):
        self.tempMemory = MemoryManager()

    def loadMemory(self):
        self.mStack.append(self.tempMemory)

    def isPointer(self,operand):
        return operand[0] == '&'

    def isDirect(self,operand):
        return operand[0] == '*'

    def initScreen(self):
        self.screen.title('Code To Paint')
        self.screen.colormode(255)
        self.screen.delay(10)
        screen_x, screen_y = self.screen.screensize()

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

        self.initScreen()

        self.requestMemory('main')
        self.loadMemory()#loads main memory segment

        while  self.instructions[self.pc].operator != operators['end']:
            instruction = self.instructions[self.pc]
            #print operators.keys()[operators.values().index(self.instructions[self.pc].operator)]
            #print instruction.result
            if instruction.operator == operators['+']:

                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                elif self.isDirect(instruction.secondOperand): #is a direct value
                    second = float(instruction.secondOperand.split('*')[1])
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'
                self.writeOnMemory(instruction.result,first + second)

            elif instruction.operator == operators['-']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first - second)

            elif instruction.operator == operators['*']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                elif self.isDirect(instruction.secondOperand): #is a direct value
                    second = float(instruction.secondOperand.split('*')[1])
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'


                self.writeOnMemory(
                instruction.result,
                first*
                second
                )

            elif instruction.operator == operators['/']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                if second == 0:
                    return 'Error, division by zero'

                self.writeOnMemory(instruction.result, first / second)

            elif instruction.operator == operators['==']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first == second)

            elif instruction.operator == operators['=']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.result): #contains array memory
                    result = self.readFromMemory(instruction.result.split('&')[1])
                else :
                    result = instruction.result

                if first is None:
                    return 'Error, variable used but not assigned'
                self.writeOnMemory(result, first)

            elif instruction.operator == operators['<']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first < second)

            elif instruction.operator == operators['>']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first > second)

            elif instruction.operator == operators['&']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first and second)

            elif instruction.operator == operators['|']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if first is None or second is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first or second)

            elif instruction.operator == operators['goto']:
                self.pc = int(instruction.result) - 1 # -1 because after this code it sums 1 before ending the cycle


            elif instruction.operator == operators['gotoF']:

                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                if not first:
                    self.pc = int(instruction.result) - 1

            elif instruction.operator == operators['gotoT']:

                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                if first:
                    self.pc = int(instruction.result) - 1

            elif instruction.operator == operators['return']:

                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.writeOnMemory(instruction.result, first)
                #retrieve last pointer to jump back where function was called
                self.pc = int(self.pointerStack.pop())

            elif instruction.operator == operators['era']:

                #loads new memory to stack
                self.requestMemory(instruction.firstOperand)

            elif instruction.operator == operators['loadMemory']:
                #loads new Memory into stack
                self.loadMemory()

            elif instruction.operator == operators['goSub']:
                #adds pointer to stack to know how to jump back after return
                self.pointerStack.append(self.pc)
                self.pc = int(instruction.result) - 1

            elif instruction.operator == operators['param']:

                # we use previous memoty because we are adding info from last memory segment before change context

                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromPreviousMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.writeOnNewMemory(instruction.result, first)

            elif instruction.operator == operators['verify']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                if first >= int(instruction.secondOperand) or first < 0:
                    return 'Error, index out of bounds'

            elif instruction.operator == operators['print']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                print(first)

            elif instruction.operator == operators['penUp']:
                self.turtle.penup()

            elif instruction.operator == operators['penDown']:
                self.turtle.pendown()

            elif instruction.operator == operators['penSize']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.pensize(first)

            elif instruction.operator == operators['penColor']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.secondOperand): #contains array memory
                    second = self.readFromMemory(self.readFromMemory(instruction.secondOperand.split('&')[1]))
                else :
                    second = self.readFromMemory(instruction.secondOperand)

                if self.isPointer(instruction.result): #contains array memory
                    third = self.readFromMemory(instruction.result.split('&')[1])
                else :
                    third = self.readFromMemory(instruction.result)

                if first is None or second is None or third is None:
                    return 'Error, variable used but not assigned'

                self.turtle.pencolor((first, second, third))

            elif instruction.operator == operators['setX']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.setx(first)

            elif instruction.operator == operators['setY']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.sety(first)

            elif instruction.operator == operators['clear']:

                self.turtle.clear()

            elif instruction.operator == operators['moveX']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                # we save last heading to restore it after draw
                lastHeading = self.turtle.heading()
                if first < 0:
                    self.turtle.setheading(180)
                    self.turtle.forward(-first)
                else :
                    self.turtle.setheading(0)
                    self.turtle.forward(first)

                self.turtle.setheading(lastHeading) # restores the initial heading

            elif instruction.operator == operators['moveY']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                # we save last heading to restore it after draw
                lastHeading = self.turtle.heading()

                if first < 0:
                    self.turtle.setheading(270)
                    self.turtle.forward(-first)
                else :
                    self.turtle.setheading(90)
                    self.turtle.forward(first)


                self.turtle.setheading(lastHeading) # restores the initial heading

            elif instruction.operator == operators['moveForward']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.forward(first)

            elif instruction.operator == operators['rotateLeft']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.left(first)

            elif instruction.operator == operators['rotateRight']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.right(first)

            elif instruction.operator == operators['circle']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)

                if first is None:
                    return 'Error, variable used but not assigned'

                self.turtle.circle(first) # restores the initial heading

            elif instruction.operator == operators['restoreMemory']:
                if self.isPointer(instruction.firstOperand): #contains array memory
                    first = self.readFromMemory(self.readFromMemory(instruction.firstOperand.split('&')[1]))
                else :
                    first = self.readFromMemory(instruction.firstOperand)
                if self.isPointer(instruction.result): #contains array memory
                    result = self.readFromMemory(instruction.result.split('&')[1])
                else :
                    result = instruction.result


                if first is None:
                    return 'Error, variable used but not assigned'
                self.writeOnPreviousMemory(result, first)

                #release memory
                self.mStack.pop()

            self.pc += 1

        self.turtle.getscreen().getcanvas().postscript(file="drawing.eps")

        return 'Process completed successfully'
