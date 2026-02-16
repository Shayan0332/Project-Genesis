# Project Genesis - Day 2: Functions

# Define a function to greet a friend
def greet_friend(name, age):
    """
    This function greets a friend based on age
    """
    if age < 18:
        print("Hello", name + "! You are young!")
    else:
        print("Hello", name + "! Adult now!")

# Main program starts here
print("Project Genesis - Day 2: Functions Example")

# Ask for three friends' names and ages
for i in range(3):
    name = input("Enter friend #" + str(i+1) + " name: ")
    age = int(input("Enter " + name + "'s age: "))
    
    # Call the function to greet friend
    greet_friend(name, age)
