#A class is a template that defines how objects are created and used

class student:
    pass

#student1 is a obj created from student class
student1=student()


student2=student()


#1.
class student:        #
    def intro(self):  
        print("hello im a unemployed kid in my house")

student1=student()
student1.intro() 
#calling the intro() method using student1 obj 

#2.
class car:
#car is a class name
    


    def __init__(self,brand,color,model):


        self.brand=brand
        self.color=color
        self.model=model 

    def display(self):


        print("brand:",self.brand)
        print("color:",self.color)
        print("model:",self.model)


car1=car('BMW',"Black","M5") 
# car1 and car 2  are objs


car2=car("Porsche","red","9 11 turbo s") 


car1.display()

car2.display()
#calling display() method using car1 and car2 objs


#print() can be used when their is no method
#print(car1.brand,car1.color,car1.model)
#print(car2.brand,car2.color,car2.model)

          
    
 
    
