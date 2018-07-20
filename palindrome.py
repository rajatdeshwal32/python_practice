word = str(input("please enter a word : "))
reverse = word[:: -1]

if word == reverse:
    print("this word is a palindrome")
else:
    print("this word is not a palindrome")
