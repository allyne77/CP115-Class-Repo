age = int(input("Enter age: "))
accident_count = int(input("Enter accident count: "))
discount_amount = 0

if age < 25:
    base_premium = 2400
elif 25 <= age <= 40:
    base_premium = 1800
elif age > 50:
    base_premium = 2000

if accident_count == 0:
    discount_amount = 0.10 * base_premium
elif accident_count <= 1 or accident_count <= 2:
    discount_amount = base_premium + 300
elif accident_count > 3:
    discount_amount = base_premium + 600

final_premium = base_premium - discount_amount


# Your code here

print(base_premium)
print(final_premium)
print(discount_amount)