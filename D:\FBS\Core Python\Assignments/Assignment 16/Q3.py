class Shirt:
    
    size_increment = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    
    def __init__(self, sid=None, sname=None, stype=None, price=0, size=None):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    
    def __del__(self):
        print("Shirt object destroyed")

    def ShowBook(self):
        final_price = self.calculateFinalPrice()
        print("Shirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.stype)
        print("Size       :", self.size)
        print("Final Price:", final_price)


    @staticmethod
    def calculatePriceBySize(price, size):
        increment = Shirt.size_increment.get(size.lower(), 0)
        return price + (price * increment / 100)

    
    def calculateFinalPrice(self):
        return Shirt.calculatePriceBySize(self.price, self.size)

s1 = Shirt(101, "Raymond", "Formal", 1000, "Small")
s1.ShowBook()

s2 = Shirt(102, "Peter England", "Casual", 1000, "Medium")
s2.ShowBook()

s3 = Shirt(103, "Louis Philippe", "Formal", 1000, "Large")
s3.ShowBook()

s4 = Shirt(104, "Arrow", "Party", 1000, "XLarge")
s4.ShowBook()