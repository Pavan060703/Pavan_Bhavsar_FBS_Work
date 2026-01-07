amount=int(input("Enter the amount"))

note_2000=amount//2000
amount=amount%2000

note_500=amount//500
amount=amount%500

note_200=amount//200
amount=amount%200

note_100=amount//100
amount=amount%100

note_50=amount//50
amount=amount%50

note_20=amount//20
amount=amount%20

note_10=amount//10
amount=amount%10

note_5=amount//5
amount=amount%5

note_2=amount/2
amount=amount%2

note_1=amount/1


total_note=note_2000+note_500+note_200+note_100+note_50+note_20+note_10

print(total_note)
