while True:

    w = (input("Enter a word: "))

    if w[::-1] == w:
        print("It is a palindrome!")
    else:
        print("Not a palindrome!")