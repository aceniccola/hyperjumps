''' HyperDict Class:
This is a class but we are using it to generate our constants 
(if this problem were to be more general we would edit this class to give our algorithm more functionallity)
'''

class hyperDict:
    
    # creates a constant object that we can get our individual constants from
    def __init__(self):
        self.fullvalid = self.getChecker()
        self.ourdict = self.generateDictionary()
    
    # input a triple and output all possible triples that it can generate
    def stepFunction(self, triple):
        #we know that each tuple is a true triple in the way we can constuct it so we can assume that the other feild exists
        other = triple[0]*10+triple[1]
        solutions = [triple[1]+triple[2], triple[1]-triple[2], 
                    triple[1]*triple[2], triple[1]/triple[2], 
                    other-triple[2], other/triple[2]]

        possibilities = []

        for solution in solutions:
            if abs(int(solution)) == solution and solution%10!=0:
                possibilities.append(int(solution%10))  

        possibilities = [*set(possibilities)]

        possibleTriples = [(triple[1], triple[2], possibilities[i]) for i in range(len(possibilities))]
        return possibleTriples

    # confirms the first three values of our sequence are a valid triple on their own (i.e. they dont require another digit to be valid)
    def getChecker(self): 
        FullValid = [0 for i in range(1000)]

        for i in range(1,9): 
            for j in range(1,9):
                for k in range(1,9):
                    if (i+j)%10 == k or (i-j)%10 == k or (i*j)%10 == k or (i/j)%10 == k:
                        FullValid[100*i+10*j+k] = 1
        return FullValid

    # creates a dictionary where the keys are triples and the values are all possible triples that can create them
    def generateDictionary(self):
        list = []
        generatedDic = {}

        for i in range(1,10):
            for j in range(1,9):
                for k in range(1,9):
                    list.append((k,j,i))

        for i in range(len(list)):
            generatedDic[list[i]] = []

        for i in range(512):
            constructObj = self.stepFunction(list[i])
            for tup in constructObj:
                generatedDic[tup].append(list[i])
        return generatedDic



