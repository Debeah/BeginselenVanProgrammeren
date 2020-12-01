# --- Initialise set ---
# Warning: set() is used for an empty set, or to turn a list into a set.
# set(float) will not work.
# For some reason, numbers = set().add(float) will not work either, as it returns None.
# Perhaps because it's trying to add an element to a set that has yet to be assigned a name?

# UPDATE:
# set() requires either an iterable or no argument, so to make line 3 work you'd need to write: set([float])
# set().add(float) is a function with no return, therefore line 4 didn't work either.
numbers = {float(input("Enter a number: "))}

while len(numbers) < 10:
    numbers.add(float(input("Enter another number")))  # set.add method has no effect when element already present

# When 10 numbers, while loop stops, print the set.
print(numbers)
