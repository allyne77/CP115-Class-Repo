monthly_income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
loan_amount = int(input("Enter loan amount: "))
interest_rate = 0
max_loan_amount = 0
approval_status = " "

if credit_score >= 700:
    interest_rate = 0.035
    credit_score == 'Excellent'
elif 600 <= credit_score < 700:
    interest_rate = 0.055
    credit_score == 'Good'
elif 500 <= credit_score < 600:
    interest_rate = 'Rejected'
    credit_score == 'Poor'
    


# Your code here

print(interest_rate)
print(max_loan_amount)
print(approval_status)