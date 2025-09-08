employee_name = input("Enter employee name :")
base_salary = float(input("Enter base salary :"))
overtime_hours = int(input("Enter overtime hours :"))
tax_status = input("Enter tax status (single, married, head) :")
total_income = float(input("Enter total income :"))


# TODO your code here

if tax_status == "single" and total_income >= 5000 :
    tax_rate == 0.22 
if tax_status == "Married" and total_income >= 6000:
    tax_rate == 0.20 
if tax_status == "Head" and total_income >= 5500 :
    tax_rate == 0.25 

epf = 0.11 * base_salary 
socso = 0.05 * base_salary
total_deduction = epf + socso

net_salary = base_salary + (overtime_hours * 20) - (base_salary * tax_rate) - total_deduction

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")

