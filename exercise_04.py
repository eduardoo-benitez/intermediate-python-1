sum = 0
count = 1
while (count <= 5):
    inp = input("Enter int #" + str(count) + ": ")

    if (inp.isdigit()):
        count += 1
        sum += int(inp)
    else:
        print("Invalid input. Please only enter an int.")

print("Your sum is: " + str(sum))


