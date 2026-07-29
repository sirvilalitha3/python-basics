#def ki a keyword to create function
#function_name is a name of the function
#() parenthesis , ':'starts the function body
print("\nFUNCTIONS")
def function_name(): 
    print("hello")
function_name()

print("\nPARAMETERS") #to pass the values
def greet(name):      #name is a parameter
    print("hello",name) 
greet("modi")         #modi is argument
greet("meloni")

print("\nRETURN VALUES")
def add(a,b):
    return a+b       #sends value back
results=add(10,20)   #results recieve the retuen value
print(results)       #displays output

print("\nSCOPES")
#LOCAL VARIABLE (inside the function)
def demo():
    x=10
    print(10)
demo()

#GLOBAL VARIABLE (A global variable is created outside all functions. It can be read from anywhere in the program)
name='lalitha'
def greet(name):
    print(name)
greet('lalitha')
print(name)

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input('enter a number:'))
if is_prime(num):
             print('prime')
else:
     print('not prime')    

