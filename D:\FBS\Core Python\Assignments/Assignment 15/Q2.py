# Create a class product with members as pid,pname , price and  quantity    
class Product:
    def __init__(self,pid,pname,price,quantity):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
    
    def showProduct(self):
        print("Product ID : ",self.pid)
        print("Product Name : ",self.pname)
        print("Prduct Price : ",self.price)
        print("Product Quantity : ",self.quantity)

    def __del__(self):
        print("Product object destroyed")
    
p=Product(101,"TeaPowder",70,20)
p.showProduct()