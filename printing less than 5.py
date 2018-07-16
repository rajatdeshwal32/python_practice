my_list = [1, 1, 2, 3, 4, 5, 8, 13, 21, 24, 34, 55, 89]

num = int(input("choose a number : "))

new_list = []

for i in my_list:
    if i < num:
        new_list.append(i)

print(new_list)
