num = int(input("Please choose a number to divide: "))

newlist = []

for i in range(1, num):
    if num % i == 0:
        newlist.append(i)

print(newlist)
