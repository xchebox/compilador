class QuadrupleManager:

    def __init__(self):
        self.quadrupleStack = []

    #adds quadruple to stack
    def addQuadruple (self, operator, operand1, operand2, result):
        self.quadrupleStack.append(Quadruple(operator, operand1, operand2, result))
        return result

class Quadruple :

    def __init__(self, operator, operand1, operand2, result):
        self.operator = operator;
        self.firstOperand = operand1;
        self.secondOperand = operand2;
        self.result = result;
