
print("Enter list of numbers. Enter z to exit.")
newlist = []
while True:
    a = input()
    if a == "z":
        break
    newlist.append(int(a))
print(newlist)

'''
Enter list of numbers. Enter z to exit.
2
3
4
1
z
[2, 3, 4, 1]
'''