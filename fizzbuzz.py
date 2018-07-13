def fizzbuzz(num):

    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizz buzz')
        elif i % 2 == 0:
            print('fizz')
        elif i % 3 == 0:
            print('buzz')
        else:
            print(i)


print(fizzbuzz(10))
