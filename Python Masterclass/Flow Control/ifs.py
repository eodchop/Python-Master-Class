name = input("Please enter your name:")
age = int(input("How old are you, {0}? ".format(name)))
print("{} is {} years of age".format(name, age))

if age >= 18:
    print("You are old enough to vote.")
    print("Please put an X in the box")
else: 
    print("You are not old enough to vote. Please come back in {0} years".format(18 - age))