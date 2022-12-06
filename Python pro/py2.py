print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
no_of_people = input("How many people to split the bill?")
float_tip = float(bill) * (int(tip)/100)
float_bill = float(bill) + float_tip
each_person = round(float_bill/int(no_of_people), 2)
print(f"Each person should pay: ${each_person}")
