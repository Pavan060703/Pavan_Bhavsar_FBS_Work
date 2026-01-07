# Create a class shirt with members as sid,sname, type ,price and size.
class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.price=price
        self.size=size

    def showShirt(self):
        print("Shirt Id : ",self.sid)
        print("Shirt Name : ",self.sname)
        print("shirt type : ",self.type)
        print("Shirt Price : ",self.price)
        print("Shirt Size : ",self.size)

    def __del__(self):
        print("Shirt object is destroyed")

s=Shirt(101,"Raymond","Format",1500,"Medium")
s.showShirt()