#rent calculator using python
rent=int(input("Enter Total Rent of Flat/Hostel= "))
food=int(input("Enter Total amount of food ordered= "))
electricity=int(input("Enter Total Electricity spend = "))
charge_spend=int(input("Enter Total charge per unit = "))
person=int(input("Enter Total Person you want to split = "))
total=(rent+food+electricity*charge_spend)//person
print("the Total split per person is ",total)