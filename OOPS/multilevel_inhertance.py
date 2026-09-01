#student class
class student():

    #student method
    def study(self):
        print(" hutt hum tho bakodi karenge")

#teacher class
class teacher(student):

    #teacher method
    def teach(self):
        print("hutt hum raaata marvangey") 

#principal class
class principal(teacher):

    #principal method
    def manage(self):
        print('principal hai hum(bandbudh aur budbak)')  

#obj of principal class
p=principal()
p.study()
p.teach()
p.manage()
                   