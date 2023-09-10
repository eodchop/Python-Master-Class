for i in range(1,13):
    print("Number {0:2} squared is {1:3} and cubed is {2:4}.".format(i, i ** 2, i ** 3))

print()
for i in range(1,13):
    print("Number {0:2} squared is {1:<3} and cubed is {2:^4}.".format(i, i ** 2, i ** 3))

print(type("Pi is approximately {0:12}".format(22 /7)))



