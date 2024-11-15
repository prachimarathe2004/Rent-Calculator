rent=int(input ("Enter your hostel/Flat rent = "))
food=int(input("Enter the amount of food ordered= "))
electricity_spend= int(input("enter the total of electricity = "))
charge_per_unit=int(input("enter the charge perunit = "))
persons = int(input("Enter the number  of persons living in room/flat = "))

total_bill=electricity_spend  * charge_per_unit 

output = (food + rent +total_bill )//persons

print("Each person will pay=", output)


