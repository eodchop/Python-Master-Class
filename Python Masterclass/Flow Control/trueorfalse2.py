#truth Value Testing
#0 = False 0.0 = False
#empty strings evaluate as false
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
#if name is not equal to an empty string
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")



