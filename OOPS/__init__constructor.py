class carrental:
    print('car rental booking')

    def __init__(self,customer,days,car_model):
          self.customer=customer
          self.days=days
          self.car_model=car_model

    def show(self):
         print("customer name:",self.customer)
         print("num of days:",self.days)
         print("car model:",self.car_model)

booking1=carrental("lily",5,"tvs")   
booking1.show()            
        