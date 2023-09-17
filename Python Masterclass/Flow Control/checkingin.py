parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print(letter)
else:
    print("Your selection {} is not in the string {}".format(letter, parrot))