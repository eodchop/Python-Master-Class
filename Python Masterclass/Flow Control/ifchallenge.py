#write a small program that asks for a name and and age
#check if the person is the right age to go on an 18-30 vacation
#must be over 18 and under 31 and if they are in this range, welcome them to the holiday,
#if under 18 or over 31, you print a message that they do not qualify
name = str(input("What is your name? "))
age = int(input("How old are you? "))
if age in range(18,31):
    print("You are {} years old. {}, enjoy your vacation!".format(age, name))
elif age not in range(18,31):
    print("{}, you are {} years of age, and therefore do not qualify".format(name, age))
# elif age > 31:
#     print("{}, {} is too old to participate.".format(name, age))
# else:
#     print("{}, {} is too young to participate.".format(name, age))
#
