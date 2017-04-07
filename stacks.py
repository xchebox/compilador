fStack = []
vStack = []



def getLastVariable():
    return vStack[len(fStack) - 1]

def getLastFunction():
    return fStack[len(fStack) - 1]
