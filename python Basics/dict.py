






student={"name":"sirvilalitha", "age":20}

#accesing
print(student)
print("name:",student['name'])
print(student["age"])
print(student.keys())
print(student.values())
print(student.items())
print(type(student))
student["grade"]='c'
print("adding elements",student)
student.update({"grade":"a+"})
print("updated",student)
student['marks']=({"maths":90,"datascience":100})
print(student)


#looping
for keys in student:
    print(student[keys])
    for keys,values in student.items():
        print(keys,values)


#===========================phone book=================
phonebook = {}
while True:
    choice = input("Add/Search/Exit: ").lower()
    if choice == "add":
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number
    elif choice == "search":
        name = input("Enter name to search: ")
        print("Number:", phonebook.get(name, "Not found"))
    elif choice == "exit":
        break
        