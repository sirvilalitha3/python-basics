sets1={1,2,"lalitha"}
print(sets1)
print(type(sets1))
#print(sets1[1]) indexing is not allowes as it is unordered but using some methods we can access ele
sets1.add(3) #inserting element
print(sets1)
sets1.discard(3)
print(sets1)
sets1.add("sindhu")
print(sets1) #new element dont have fixed position
#sets1.pop('lalitha')
#print(sets1)    
numbers = {1, 2, 3, 4}
removed = numbers.pop()
print("Removed:", removed)
print("Updated set:", numbers)
#the removed element is stored in the variable removed so you can use it later


#=======================common friend finder=================
friends_A = {"Alice", "Bob", "Charlie"}
friends_B = {"Bob", "David", "Charlie"}

common = friends_A & friends_B
print("Mutual friends:", common)
 #=======================shopping list duplicate removes=============
shopping_list = ["apple", "banana", "apple", "orange", "banana"]
unique_items = set(shopping_list)
print("Unique shopping list:", unique_items)

#=====================sets calculator===========
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric Difference:", A ^ B)

 #=================lottery============================
import random

participants = {"Alice", "Bob", "Charlie", "David"}
winner = random.choice(list(participants))
print("Winner:", winner)
