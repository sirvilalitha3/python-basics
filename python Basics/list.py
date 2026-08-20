#a=[1,2,3]
#mixed_datatype=[23,'lalitha',8.44,True]

fruits=["orange","grape","banana"] 
#===============================accessing the elements========================
print(fruits) #give output as list
print(fruits[0]) #to access any element we use index
print(fruits[-1])
print(fruits[0:3:1])


 #====================================nested list======================================
list=[[1,2,3],[2,3]]
print(list[0][0])


#================================================loops============================================
list=[[1,2,3],[35,75,4]]
for lists in list:
    print(lists)

fruits=["mango","pineapple",'KIWI']
for fruit in fruits:
    print(fruit)  

 #==================================adding elements==================================================  
names=["lalitha","sindhu"]
names.append("jotu")        #append add elemnt at end we have to use diffline for the method 
print(names)
names.insert(0,'meghana')   #insert add elemnt acc to index you mentioned
print(names)
more=["sathvika","varsha"]
names.extend(more)          #extend adds two list
print(names)


#==============================REMOVING=====================================
names.remove("meghana")
print(names)
names.pop(2)
print(names)
names.clear()
print(names)
#del keyword,remove elements by slicing,loops
numbers=[1,3,5,79,2,4,6,8,10]
numbers=[num for num in numbers if num%2==0] #by loops
print(numbers)
numbers[1:3]=[]        #by slicing
print(numbers)
del numbers[1]     #by del keyword


#============================LIST METHODS==================================================
numbers=[1,5,6,0,53,1,5]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
movies=["3idiots","bahubali","RRR"]
movies.sort(key=len)
print(movies)
print(len(movies))
movies.reverse()
print(movies)
position=movies.index("RRR")
print(position)
occurence=numbers.count(1)
print(occurence)
print(movies.copy())
print(max(numbers))
print(min(numbers))
print(sum(numbers))
foods=["dalrice","biryani","potatorice"]
for index , food in enumerate(foods):
    print(foods)
    sentence="".join(foods)
    print(sentence)


#=====================================opeartors=========================================  
list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)  #concatetation
print(list1*3)       #repetation
print(1 in list1)    #membership

#=================to dolist===================
tasks = []
while True:
    choice = input("Add/Remove/Show/Exit: ").lower()
    if choice == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "remove":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
    elif choice == "show":
        print("Tasks:", tasks)
    elif choice == "exit":
        break
