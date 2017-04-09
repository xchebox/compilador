class QuadrupleManager:

    def __init__(self):
        self.quadrupleStack = []
        self.counter = 0

    #adds quadruple to stack
    def addQuadruple (self, operator, operand1, operand2, result):
        self.quadrupleStack.append(Quadruple(operator, operand1, operand2, result))
        self.counter += 1
        return result

    def getCounter(self):
        return self.counter

    def fillQuadrupleJump(self, indexOfQ, whereToJump):
        self.quadrupleStack[indexOfQ].setJump(whereToJump)

class Quadruple :

    def __init__(self, operator, operand1, operand2, result):
        self.operator = operator
        self.firstOperand = operand1
        self.secondOperand = operand2
        self.result = result

    def setJump(self, jump):
        self.result = jump
