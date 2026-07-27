# Arithmetic Operators
print('\n===========ARITHMETIC OPERATORS============')
a = 20
b = 6

print("Addition:", a + b)         
print("Subtraction:", a - b)      
print("Multiplication:", a * b)   
print("Division:", a / b)         
print("Floor Division:", a // b)  
print("Modulus:", a % b)          
print("Exponent:", a ** b)       

# Comparison Operators
print('\n=========COMPARISON OPERATORS===========')
a = 10
b = 20

print(a == b)   #eualsto
print(a != b)   #notequal
print(a > b)    #greaterthan
print(a < b)    #lessthan
print(a >= b)   #greater and euals
print(a <= b)   #less and equal

# Assignment Operators
print('\n=========ASSIGNMENT OPERATOR===========')

x = 10
print(x)

x += 5  #x=x+5=15
print(x)

x -= 3   
print(x)

x *= 2
print(x)

x /= 4
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)

# Logical Operators
print('\n=========LOGICAL OPERATOR===========')
a = 15
b = 8

print(a > 10 and b < 10)   #and: return true if both statement are true
print(a < 10 or b < 10)    # or:return true if one of the statement is True
print(not(a > 10))         # not:reverse the result

# Membership Operators
print('\n=========MEMBERSHIP OPERATOR=========')
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)     
print("Orange" in fruits)     
                                 #in and not in gives the results based on the value is present in a variable 
print("Orange" not in fruits)

# Bitwise Operators
print('\n=========BITWISE OPERATOR========')
a = 5     
b = 3      

print(a & b)   
print(a | b)  
print(a ^ b)   
print(~a)      
print(a << 1)  
print(a >> 1)  

# Identity Operators
print('\n=======IDENTITY OPERATORS=======')
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)       # True
print(x is z)       # False

print(x is not z)   #true