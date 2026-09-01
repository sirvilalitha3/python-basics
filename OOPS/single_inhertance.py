class parent:

    #parent class
    pass

class child(parent):

    #child class
    pass

class dog():
    def bark(self):
        print("bow bow chimtu bhAAI bolte")

class puppy(dog):
    def play(self):
        print("puppy is playing")   


pup=puppy()
pup.bark()
pup.play()            