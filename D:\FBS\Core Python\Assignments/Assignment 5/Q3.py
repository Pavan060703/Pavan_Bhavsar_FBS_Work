passengers=int(input("Enter number of passengers"))
ticket_cost=float(input("Enter cost per ticket"))
total_amount=0
for i in range(passengers):
    age=int(input(f"Enter age of passenger {i+1}: "))

    if age<12:
        discount=ticket_cost*0.30
        final_cost=ticket_cost-discount
    elif age>59:
        discount=ticket_cost*0.50
        final_cost=ticket_cost-discount
    else:
        final_cost=ticket_cost

    print(f"Ticket cost for passenger {i+1}:{final_cost:.2f}")
    total_amount+=final_cost

print(f"\nTotal amount to be paid for all passengers :{total_amount:.2f}")
