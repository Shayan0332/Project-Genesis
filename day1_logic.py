# Project Genesis - Day 1: Loops & Conditions

# Print a header so user knows what this program does
print("Project Genesis - Day 1: Loops & Conditions")

# Start a loop that repeats 3 times
# 'i' will take values 0, 1, 2
for i in range(3):
    
    # Ask the user for the name of friend #i+1
    # i+1 because humans start counting from 1, not 0
    name = input("Enter friend #" + str(i+1) + " name: ")
    
    # Ask the user for that friend's age and convert it to integer
    age = int(input("Enter " + name + "'s age: "))
    
    # Check if age is less than 18
    if age < 18:
        # If true, print a special message for young friends
        print("Hello", name + "! You are young!")
    else:
        # If false (age >= 18), print a message for adults
        print("Hello", name + "! Adult now!")

