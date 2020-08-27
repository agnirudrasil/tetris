inp = input("Enter a number or word: ")

if inp[::-1].lower() == inp.lower():
    print("Palindrome")
else:
    print("Not Palindrome")
