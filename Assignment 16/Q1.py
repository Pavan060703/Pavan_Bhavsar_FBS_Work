class Book:
    count=0
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

        Book.count+=1

    def showBook(self):
        print("Book Id:",self.bid)
        print("Book Name:",self.bname)
        print("Book Price:",self.price)
        print("Book Author:",self.author)
        

    def __del__(self):
        print("Book object is destroyed")

b1=Book(101,"ShrimanYogi",610,"Ranjeet Desai")
b2=Book(102,"Bhootacha Khel",400,"Pramod Naikwade")
print(f"There are {Book.count} book objects")
li=[b1,b2]
for i in li:
    print("-----------------------------------")
    i.showBook()
