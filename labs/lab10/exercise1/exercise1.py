position = input("Enter position: ")
overtime_hours = int(input("Enter overtime hours:"))
is_weekend = input("Is it weekend (yes/no):")
hourly_rate = 0
weekend_bonus = 5


if position == "Manager":
    hourly_rate = 35

elif position == "Supervisor":
    hourly_rate = 25

elif position == "Staff":
    hourly_rate = 18


overtime_pay = overtime_hours * hourly_rate * (5 if is_weekend.lower() == "yes" else 1)
total_pay = (hourly_rate * 40) + overtime_pay 
total_pay += weekend_bonus if is_weekend.lower() == "yes" else 0



# Your code here

print(hourly_rate)
print(overtime_pay)
print(total_pay)