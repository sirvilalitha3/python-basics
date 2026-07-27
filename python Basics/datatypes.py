
print("STUDENTS DATA")
#STRING (stores characters)
name=input('enter student name') 

#INTEGER(stores whole/integer numbers)
age=int(input('enter age:')) 

#FLOAT(stors decimal numbers)
cgpa=float(input("enter cgpa:"))  

#BOOLEAN(stores true/false values)
hostel = input("Hosteller? (yes/no): ").lower()
is_hosteller = hostel == "yes"


# LIST[stores multiple values] ,ordered and mutable
subjects = input("Enter Subjects (comma separated): ").split(",")  
print(subjects[0])

# TUPLE (stors multiple values)  ,orderd and immutable
marks = tuple(map(int, input("Enter 3 Marks (space separated): ").split())) # map() is used to apply the int() function to every element.


# SET {stores unique values}, unordered and mutable
skills = set(input("Enter Skills (space separated): ").split())


# {DICTIONARY :stores data in key-value pair} , ordered and mutable
student = {
    "Name": name,
    "Age": age,
    "CGPA": cgpa,
    "Hosteller": is_hosteller,
    "Subjects": subjects,
    "Marks": marks,
    "Skills": skills
}


print('\n======OUTPUT=====')
#OUTPUT
print('name:',name)
print("age:",age)
print('cgpa;',cgpa)
print('hosteller:',hostel)
print('subjects;',subjects)
print('marks:',marks)
print('skills:',skills)

print("\n========== DATA TYPES ==========") 

print("Name:", type(name)) #type() is to check the type of a varible
print("Age:", type(age))
print("CGPA:", type(cgpa))
print("Hosteller:", type(is_hosteller))
print("Subjects:", type(subjects))
print("Marks:", type(marks))
print("Skills:", type(skills))
print('student:',type(student))
print(id(name)) #id() is to get address of object



