#encapsulation means hiding data and controlling access through methods


class secretdiary:
    def __init__(self,owner):
        self.owner=owner

        self.__entries=[]
        #enties(public),_entries(protected),__entries(private)
    
    #method to enter data
    def add_entry(self,entry):
        self.__entries.append(entry)
        print("entry added successfully")  

    #method to view entries
    def view_entries(self):
        for entry in self.__entries:
            print(entry)  

#object
diary=secretdiary('heeeeeeeeeeeee lalalalalitha')
print(diary.owner)        

#adding entries
diary.add_entry("dear diary,today i learned encapsulation topic,today its sound like lalalalalalalal G lagaye")
diary.add_entry("yeh kya bakchodi hai bhut maaza araha")
diary.add_entry("~etlu mi lalitha")

#view entries
diary.view_entries()
      