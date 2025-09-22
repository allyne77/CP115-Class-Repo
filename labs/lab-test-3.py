monthly_usage = int(input("Enter monthly usage: "))
amount_bill = int(input("Enter amount bill: "))


if monthly_usage < 50:
    discount_amount = 0
    final_bill = amount_bill

elif monthly_usage <= 100:
    discount_amount = 0.05 
    final_bill = discount_amount * amount_bill
   
elif monthly_usage > 100:
    discount_amount = 0.20 
    final_bill = discount_amount * amount_bill
    
amount_bill_pay = amount_bill - discount_amount * amount_bill

print(amount_bill_pay)




