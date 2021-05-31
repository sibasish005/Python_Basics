class Train:
    def __init__(self,name,seat,price):
        self.name = name
        self.seat = seat
        self.price = price
    
    def getinfo(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The no. of seats available in the train is {self.seat}")
        print("************")
    
    def priceInfo(self):
        print(f"The price of Ticket is {self.price}")
        print("************")
    
    def ticket(self):
        if self.seat > 0:
            print("Congratulation! Your ticket is booked")
            self.seat = self.seat -1
            print(f"Available ticket is {self.seat}")
            print("************")
        else:
            print("All seats are booked please try any other train")

a = Train("Rajdhani Express",100,356) 
a.getinfo()
a.priceInfo()
a.ticket() 