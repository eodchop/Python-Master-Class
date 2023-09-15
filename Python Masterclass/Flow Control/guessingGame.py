answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("You guessed too low.")
        guess = int(input())
    else:
        print("You guessed too high. Please guess lower.")
        guess = int(input())
    if guess == answer:
        print("Well done. You chose wisely.")
    else:
        print("Sorry you chose incorrectly.")
else:
    print("You chose wisely!")



# if guess < answer:
#     print("Ha ha. You're a failure. Too Low.")
#     guess = int(input("Please guess again: "))
#     if guess == answer:
#         print("Well Done. You guessed it.")
#     else:
#         print("You have not guessed correctly.")
# elif guess > answer:
#     print("Ha ha. You're a failure. You guessed too high.")
#     guess = int(input("Please guess again: "))
#     if guess == answer:
#         print("Well done. You chose wisely.")
#     else:
#         print("You have not guessed correctly.")
# else:
#     print("You guessed right")



