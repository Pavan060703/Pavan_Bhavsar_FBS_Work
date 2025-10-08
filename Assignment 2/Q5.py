cost_price=float(input("Enter the cost price of book"))
discount=float(input("Enter the discount on book"))

discount_price=(discount/100)*cost_price

selling_price=cost_price-discount_price

print("Selling price of book ",selling_price)
