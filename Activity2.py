string = input("Please enter your own string: ")

string2 = ("")
for i in string:
    string2 = i + string2

print("\nOriginal string is = ", string)
print("Reversed string is = ", string2)