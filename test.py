"""working (although ugly) implementation of our task; created for testing purposes"""

list = []
for i in [1,2,3,4,5,6,7,8,9]:
    for j in [1,2,3,4,5,6,7,8]:
        for k in [1,2,3,4,5,6,7,8]:
            list.append((k,j,i))


def getKey(list, tuple):
    for i in range(len(list)):
        if list[i] == tuple: return i
    return

def construction(triple):

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

    possibleTriples = [(triple[1],triple[2], possibilities[i]) for i in range(len(possibilities))]
    
    return possibleTriples

generatorDic = {}
generatedDic = {}
FullValid = [0 for i in range(1000)]
for i in range(8):
    i+=1
    for j in range(8):
        j+=1
        for k in range(8):
            k+=1
            if (i+j)%10 == k or (i-j)%10 == k or (i*j)%10 == k or (i/j)%10 == k:
                FullValid[100*i+10*j+k] = 1

for i in range(512):
    generatorDic[list[i]] = []

for i in range(len(list)):
    generatedDic[list[i]] = []

for i in range(512):
    constructObj = construction(list[i])
    for tup in constructObj:
        generatedDic[tup].append(list[i])
        generatorDic[list[i]].append(tup)

choices0 = [1,1,3,4,7,7,8,8]
path = []

def reversed(list):
    newList = []
    for i in range(len(list)):
        newList.append(list[-i])
    newList.remove(9)
    newList.append(9)
    return newList

def copCre(copied, lost):
    copy = copied.copy()
    copy.remove(lost)
    return copy


fin7, fin6, fin5 = (0,0,0)
sec8, sec7, sec6, sec5 = ([0],[0,0],[0,0,0],[0,0,0,0])

for choice0 in choices0:
    choices1 = copCre(choices0, choice0)
    for choice1 in choices1:
        choices2 = copCre(choices1, choice1)
        # from here on everything is reflexive
        for nextTuple in generatedDic[(choice1, choice0, 9)]:
            if nextTuple[0] in choices2: 
                choices3 = copCre(choices2, nextTuple[0])
                for nextTuple2 in generatedDic[nextTuple]:
                    if nextTuple2[0] in choices3: 
                        choices4 = copCre(choices3, nextTuple2[0])
                        for nextTuple3 in generatedDic[nextTuple2]:
                            if nextTuple3[0] in choices4: 
                                choices5 = copCre(choices4, nextTuple3[0])
                                for nextTuple4 in generatedDic[nextTuple3]:
                                    if nextTuple4[0] in choices5: 
                                        choices6 = copCre(choices5, nextTuple4[0])
                                        for nextTuple5 in generatedDic[nextTuple4]:
                                            if nextTuple5[0] in choices6: 
                                                choices7 = copCre(choices6, nextTuple5[0])
                                                for nextTuple6 in generatedDic[nextTuple5]:
                                                    if nextTuple6[0] in choices7: 
                                                        choices8 = copCre(choices7, nextTuple6[0])
                                                        if FullValid[nextTuple6[0]*100+nextTuple5[0]*10+nextTuple4[0]] == 1:
                                                            sec8[0] = (nextTuple6[0], nextTuple5[0], nextTuple4[0], nextTuple3[0], nextTuple2[0], nextTuple[0], choice1, choice0, 9)
                                                            print(sec8[0])
                                                if FullValid[nextTuple5[0]*100+nextTuple4[0]*10+nextTuple3[0]] == 1:
                                                    if fin7 == 2: 
                                                        break
                                                    sec7[fin7] = (nextTuple5[0], nextTuple4[0], nextTuple3[0], nextTuple2[0], nextTuple[0], choice1, choice0, 9)
                                                    fin7+=1
                                        if FullValid[nextTuple4[0]*100+nextTuple3[0]*10+nextTuple2[0]] == 1:
                                                    if fin6 == 3: 
                                                        break
                                                    sec6[fin6] = (nextTuple4[0], nextTuple3[0], nextTuple2[0], nextTuple[0], choice1, choice0, 9)
                                                    fin6+=1
                                if FullValid[nextTuple4[0]*100+nextTuple3[0]*10+nextTuple2[0]] == 1:
                                    if fin5 == 4: 
                                        break
                                    sec5[fin5] = (nextTuple4[0], nextTuple3[0], nextTuple2[0], nextTuple[0], choice1, choice0, 9)
                                    fin5+=1
                
print(sec8)
print(sec7)
print(sec6)
print(sec5)
                                    
#print(nextTuple6[0], nextTuple5[0], nextTuple4[0], nextTuple3[0], nextTuple2[0], nextTuple[0], choice1, choice0, 9)
#print(generatedDic)
