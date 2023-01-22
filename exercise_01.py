def uniqueList(list):
    newList = []
    for l in list:
        if newList.count(l) == 0:
            newList.append(l)
    return newList

list = [1,6,4,6,7,1,2,5,3]

newList = uniqueList(list)

print(newList)