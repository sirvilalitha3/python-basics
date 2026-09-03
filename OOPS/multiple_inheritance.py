#multiple inheritance means one child can inherts more than one parent 
#syntax
# class parent1:

    #methods/properties
    #pass
#class parent2:

    #methods/properties
    #pass
#class child(parent1,parent2):

    #methods/properties
    #pass

#example

#parentclass 1
class alluarjun:

    #properties
    father_name ="alluarjun"
    father_profession ="actor"

     #method
    def show_father( self ):
        print("father:",self.father_name)
        print('profession:',self.father_profession)

#parentclass 2
class sneha:

    #properties
    mother_name="sneha" 
    mother_profession='entrepreneur' 

    #mthods
    def show_mother(self):
        print("mother:",self.mother_name)
        print("profession:",self.mother_profession)  

#child class inhertis both alluarjun and sneha class
class ayan(alluarjun, sneha):

    #properties
    name="ayan"    
    hobbies="teetahook panulu"

   #method
    def show_child(self):
        print('child:',self.name)
        print("hobbies:",self.hobbies) 

#creating child obj
a=ayan()

#child obj 
a.show_father()
a.show_mother()
a.show_child()

    


    