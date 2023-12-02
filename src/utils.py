#reverses list 2 levels down 
def reversedFull(forwardList):
    return [[[deepElem[-i] for i in range(1,len(deepElem)+1)] for deepElem in elem] for elem in forwardList]

# copies a list with on element `lost` (removed)
def copCre(copied, lost):
    copy = copied.copy()
    copy.remove(lost)
    return copy
