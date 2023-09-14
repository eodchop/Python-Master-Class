name = input("Please enter your name:")
age = int(input("How old are you, {0}? ".format(name)))
print("{} is {} years of age".format(name, age))

if age >= 18:
    print("You are old enough to vote.")
elif age == 900:
    print("You're older than Yoda, and should not vote")
else: 
    print("You are not old enough to vote. Please come back in {0} years".format(18 - age))

if age < 18:
    print("You are not old enough to vote. Please come back in {0} years".format(18 - age))



