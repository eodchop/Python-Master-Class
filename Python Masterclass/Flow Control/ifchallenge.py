#write a small program that asks for a name and and age
#check if the person is the right age to go on an 18-30 vacation
#must be over 18 and under 31 and if they are in this range, welcome them to the holiday,
#if under 18 or over 31, you print a message that they do not qualify

age = int(input("How old are you? "))
name = str(input("What is your name? "))

if age in range(18,31):
    print("You are {} years old. {}, enjoy your vacation!".format(age, name))
elif age > 31:
    print("{}, {} is too old to participate.".format(name, age))
else:
    print("{}, {} is too young to participate.".format(name, age))

