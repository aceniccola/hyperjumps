from hyperjumpsDic import hyperDict
import utils
import sys

# global vaiables used in hyperRec
record = [5,6,7,8]
records = [[],[],[],[]]

# global constants used in hyperRec 
DICTOBJ = hyperDict()
FULLVALID = DICTOBJ.fullvalid
OURDICTIONARY = DICTOBJ.ourdict

''' hyperRec():
*   Our recusive function that allows us to traverse though the dictionary and keep track of depth, 
*   all the while we can keep some global varibles and copyable (storage) varibles. 
'''
def hyperRec(theseChoices, depth=-1, currentPath = [0 for i in range(9)], thisTuple = (0,0,0)):

    depth += 1 # to avoid repeating this line we put it in the begining (this means that we should start out with depth = -1)

    # we start at the end. i.e. with the `9` in our sequence

    # are we in our first inital base case (in the begining - gives us the first (technically last) - number of our sequence)
    if depth==0:
        currentPath[depth] = 9
        hyperRec(theseChoices, depth, currentPath)

    # are we in our second inital base case (in the begining - after this we have our first triple)
    elif depth <= 2: 
        for choice in theseChoices:
            nextChoices = utils.copCre(theseChoices, choice)
            currentPath[depth] = choice
            hyperRec(nextChoices, depth, currentPath, (currentPath[2], currentPath[1], currentPath[0]))

    # are we in our terminal base case (ending) *NO RECURSING BEYOND THIS*
    elif depth == 9: return 

    # we need to handle recursive step here
    else:
        for nextTuple in OURDICTIONARY[thisTuple]:
                if nextTuple[0] in theseChoices: 
                    nextChoices = utils.copCre(theseChoices, nextTuple[0])
                    currentPath[depth] = nextTuple[0]

                    itWorks = FULLVALID[currentPath[depth]*100+currentPath[depth-1]*10+currentPath[depth-2]]

                    # do we record this mapping? no if we aren't deep enough or if we already recorded enough
                    # also no if it doesn't work or if we already somehow recorded the mapping before. 
                    if depth in record and len(records[depth-5])<(9-depth) \
                        and itWorks and currentPath[:depth+1] not in records[depth-5]: 

                        # we append our list of finial anwsers by a list 
                        records[depth-5].append(currentPath[:depth+1])

                    hyperRec(nextChoices, depth, currentPath, nextTuple)

def main():
    list = input("give 8 planets (numerals 1-8 and seperate elements by a space): \n")
    hyperRec([int(elem) for elem in list.split()])
    for oneList in utils.reversedFull(records):
        for elem in oneList:
            print("-----------------------------")
            print(elem)
            print("-----------------------------")
            print(" ")

if __name__ == "__main__":
    main()
