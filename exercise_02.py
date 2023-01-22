
def commonDict(d1, d2):

    commonDict = {}

    for key in d2:
        if key in d1:
            commonDict[key] = d2[key] + d1[key]
         
    return(commonDict)

d1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
d2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = commonDict(d1, d2)
print(combined_dict)