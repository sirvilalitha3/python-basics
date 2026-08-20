name="lalitha is a good girl"
lastname="choudhary"
print(name+lastname) #concatination

#========INDEXING AND SLICING========
print(name[1]) #accessing the element
print(name[-1]) #negative slicing
print(name[1:5]) #starting from 1 to n-1
print(name[1:6:1]) #start 1 stop at 6 steps 1
print(name[1:6:2]) 
print(name[::2]) #taking 2 steps from starting
print(name[2::])
print(name[2:])

print(name*3) #repetation
print("good" in name) #membership

#======================PALINDROME===========================
text=input("enter a word:")
cleaned=text.replace(' ','').lower() #to remove spacess and lower()to covert all string in small leters
if cleaned==cleaned[::-1]:   #condition actual word and when we reverse it should be equal
    print("palindrome")
#if cleaned==text.reverse(): this is wrong beacause reversed is used in list so to use it we have to convert string into a list
 #   print("palindromemada ")
else:
    print("not palindrome")

#============================ANAGARM WORDS=======================================
word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if sorted(word1) == sorted(word2):
    print("Anagram!")
else:
    print("Not an anagram.")

    ###Here are the most frequently used:

#Case Conversion

#str.upper() → "hello".upper() → "HELLO"

#str.lower() → "HELLO".lower() → "hello"

#str.title() → "hello world".title() → "Hello World"

#vTrimming

#str.strip() → removes whitespace from both ends

#str.lstrip() / str.rstrip() → remove from left/right only

#Searching

#str.find("sub") → returns index of substring or -1

#str.index("sub") → like find() but raises error if not found

#str.startswith("prefix"), str.endswith("suffix")

#Replacing
#str.replace("old", "new")
 # Splitting & Joining

#str.split(" ") → "a b c".split(" ") → ['a','b','c']

#" ".join(['a','b','c']) → "a b c"

#Checking

#str.isalpha() → only letters

#str.isdigit() → only digits

#str.isalnum() → letters + digits

#str.isspace() → only whitespace
#=============================password strength checker===============================
password=input('enter password:')
if (len(password) >=10 and 
    any(ch.islower() for ch in password) and
    any(ch.isupper() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(ch in "@#$^&*~" for ch in password)):
    print("srtong password")
else:
    print("weak password")    

#==================================vowels and consonents========================
    

    