from memory import MemoryManager
from quadruple import Quadruple
from operators import operators

class VirtualMachine:

    def __init__(self):

        # instance of memory
        self.memoryManager = MemoryManager()
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
            print q
            self.instructions[ic] = Quadruple(q[0], q[1], q[2], q[3])
            ic += 1

    def run(self):
        while self.instructions[ic] != operators['end']:
            if self.instructions[ic] == operators['+']:
                print '+'
            elif self.instructions[ic] == operators['*']:
                print '*'
            elif self.instructions[ic] == operators['/']:
                print '/'
            elif self.instructions[ic] == operators['==']:
                print '=='
            elif self.instructions[ic] == operators['=']:
                print '='
            elif self.instructions[ic] == operators['<']:
                print '<'
            elif self.instructions[ic] == operators['>']:
                print '>'
            elif self.instructions[ic] == operators['&']:
                print '&'
            elif self.instructions[ic] == operators['|']:
                print '|'
            elif self.instructions[ic] == operators['goto']:
                print 'goto'
            elif self.instructions[ic] == operators['gotoF']:
                print 'gotoF'
            elif self.instructions[ic] == operators['gotoT']:
                print 'gotoT'
            elif self.instructions[ic] == operators['return']:
                print 'return'
            elif self.instructions[ic] == operators['era']:
                print 'era'
            elif self.instructions[ic] == operators['goSub']:
                print 'goSub'
            elif self.instructions[ic] == operators['param']:
                print 'param'
            elif self.instructions[ic] == operators['end']:
                print 'end'
