# ===========================
# INPUT
# ===========================

# Takes the user's name (string)
name = input("Enter your name: ")

# Takes the user's age and converts it to an integer
age = int(input("Enter your age: "))

# Takes the user's height and converts it to a float
height = float(input("Enter your height: "))

# Takes hobbies separated by commas and stores them in a list
hobbies = input("Enter your hobbies: ").split(",")

# ===========================
# OUTPUT
# ===========================

print("\n===== USER INFORMATION =====")

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hobbies:", hobbies)

#formatting output
print('my name is {} and im {} years old,my hobbies are {} '.format(name,age,hobbies))

#f-string
print(f'my name is {name}and im {age} yrs old')
