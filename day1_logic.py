# Project Genesis - Day 1: Loops & Conditions

print("Project Genesis - Day 1: Loops & Conditions")

# Start a loop that repeats 3 times
for i in range(3):
    name = input("Enter friend #" + str(i+1) + " name: ")
    age = int(input("Enter " + name + "'s age: "))
    if age < 18:
        print("Hello", name + "! You are young!")
    else:
        print("Hello", name + "! Adult now!")

