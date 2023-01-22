
def stringDict(str):

    str = str.lower()

    dict = {}

    for c in str:
        if not c == " ":
            if c in dict:    
                dict[c] += 1
            else:                    
                dict[c] = 1
    return dict

input = input("Enter a string: ")
dict = stringDict(input)
print(dict)