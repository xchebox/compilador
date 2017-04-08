fStack = []
vStack = []
dCounter = 0



def getLastVariable():
    return vStack[len(vStack) - 1]

def getLastFunction():
    return fStack[len(fStack) - 1]
