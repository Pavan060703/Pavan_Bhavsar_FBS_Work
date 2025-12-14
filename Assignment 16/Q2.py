class Product:
    discount=10
    def __init__(self,pid,pname,price,quantity):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def showProduct(self):
        print("Product ID:",self.pid)
        print("Product Name:",self.pname)
        print("Product Price:",self.price)
        print("Product Quantity:",self.price)

    @staticmethod
    def calculateDiscount(price):
        return (Product.discount/100)*price
p=Product(101,"TeaPowder",150,20)
p.showProduct()
print(Product.calculateDiscount(p.price))

    
    