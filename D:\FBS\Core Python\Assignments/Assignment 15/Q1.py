# Create a class book with members as bid,bname,price and author . 
class Book:
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

    def showBook(self):
        print("Book id : ",self.bid)
        print("Book Name : ",self.bname)
        print("Book Price : ",self.price)
        print("Book author : ",self.author)

    def __del__(self):
         
        print("Book Object is destroyed")

b=Book(1,"ShrimanYogi",610,"Ranjeet Desai")
b.showBook()