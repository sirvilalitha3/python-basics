class Demo:
    def instance_method(self):   # needs object
        print("Instance method")

    @classmethod
    def class_method(cls):       # works on class
        print("Class method")

    @staticmethod
    def static_method():         # independent
        print("Static method")

#==============instance methode===================
# Instance Method Example
# Daily life: Student details

class Student:

    # Instance method
    def show_details(self):
        print("Name: Riya")
        print("Course: Python")
        print("Age: 21")


# Creating object
student1 = Student()

# Calling instance method
student1.show_details()

#========================class method====================
# Class Method Example
# Daily life: Company information

class Company:

    company_name = "ABC Technologies"

    # Class Method
    @classmethod
    def show_company(cls):

        # cls refers to the class
        print("Company Name:", cls.company_name)


# Calling class method using class
Company.show_company()