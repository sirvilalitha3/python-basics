#WHILE LOOP (repeats a block of code as long as a given condition is True.
print("=====WHILE LOOP EXAMPLES=====")
print("\nPROGRAM1")
i=0
while i<=10:
    print("i=",i)
    i+=1

print('\nPROGRAM2') #table
i=1
while i<=10: #executes till 10
    print("2 x",i,"=",i*2)
    i+=1 #increment

print('\nPROGRAM3')
#taking terms from the user
terms=int(input("enter the number of terms:"))

#first fibonacci number
current=0

#second fibonacci number
nextterm=1

#to track how many numbers are printed
count=0

#if the user entered invalid number
if terms==0:
    print("enter a positive number")

#if user wants only one term
elif terms==1:
    print("fibonacci sequence")
    print(current)

#if user wants more than one term
else:
    print('fibonacci sequence')


    while count<terms:        #repeats until required number of terms
        print(current)        # example for loop 1: 0  (print the current fibonacci number)
        temp=current+nextterm #temp=0+1               (adding first and second number to get next fibonacci) 
        current=nextterm      #current=1              (move the second number to first position)
        nextterm=temp         #nextterm=1             (store newly calculated number in second position)
        count+=1              #0+1                    (increase the counter for next number)

print("\nFOR LOOP EXAMPLES")
#FOR LOOP (repeats a block of code as long as a given condition is True.)
print("\nPROGRAM1")

#loop from 1 to 67(n-1)
for i in range(1,68):  # range() generates a sequence of numbers.
    print("67")        

print('\nPROGRAM2')
number=int(input("enter a number:"))
even=0
odd=0
for i in range(number):
    if i%2==0:
         even=even+i
else:
    odd=odd+i
    print(even)
    print(odd)
    
print("\nPROGRAM3")
# Program to find the factorial of a number

# Get a number from the user
num = int(input("Enter a number: "))

# Start factorial with 1 because multiplying by 1 doesn't change the result
factorial = 1

# Loop from 1 to the entered number (inclusive)
for i in range(1, num + 1):

    # Multiply the current factorial by i
    factorial = factorial * i

# Display the final factorial
print("Factorial =", factorial)
