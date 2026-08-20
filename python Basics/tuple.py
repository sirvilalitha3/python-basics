tuples=(1,2,3)
a,b,c=tuples #unpacking
print(tuple)

my_string="hello"
print(tuple(my_string))  #converting
print(tuples[1])
print(a)

#================METHODS===================================
print(tuples.count(1))  #no of elements
print(tuples.index(1))   #wht elemnt is their at wht index
for tuplee in tuples:    #looping
    print(tuplee)

#=======================ADDING============================
    
new_tuple=tuples+(10,)
print(new_tuple)
print(list(tuples))


#=================OPEARTIONS===========================
tuple1=(1,)
tuple2=(2,3,4)
print(tuple1+tuple2) #concatenation
print(tuple1*10)     #repetation

print(10 in tuple2)  #membership


#================student records=================
students = [
    ("Alice", 101),
    ("Bob", 102),
    ("Charlie", 103)
]

for name, roll in students:
    print(f"Name: {name}, Roll: {roll}")
