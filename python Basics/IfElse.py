print("\nPROGRAM 1")
print('Finding the largest number among three')
#taking input from user
a=int(input('enter first number:'))
b=int(input('enter second number:'))
c=int(input('enter third number:'))

if a==b==c:
     print('all three numbers are equal')

elif a>=b and a>=c:       # Check if num1 is greater than or equal to both num2 and num3
     print("first number is largest")

elif b>=a and b>=c:     #If the above condition is false, check if num2 is the largest
     print("second number is largest")

    

else:                 ## If neither num1 nor num2 is the largest, then num3 is the largest
     print('third number is largest')


print('\nPROGRAM 2')
print("checking if entered year is leap or not")
year=int(input("enter a year:"))
if year % 4==0:
     if year% 100==0:
          print(f"{year} is a leap year")
else:
    print(f'{year} is not a leap year')





