age = 24
print("My age is " + str(age) + " years old")
print("My age is {0} years old".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "July", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, July, Aug, Oct, and Dec".format(31))
print ("Jan: {1}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2} June: {1}, July: {2}, Aug: {1}, Sept: {1}, Oct: {2}, Nov: {1}, Dec: {2}" \
       .format(28, 31, 30))

print()
print("""Jan: {1}
      Feb: {0}
      Mar: {2} 
      Apr: {1}
      May: {2}
      Jun: {1}
      Jul: {2}
      Aug: {1}
      Sep: {1}
      Oct: {2}
      Nov: {1}
      Dec: {2}""".format(28,31, 30))