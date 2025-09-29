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
    


# Determine max loan amount (5x income)
max_loan_amount = monthly_income * 5

# Determine interest rate based on credit score
if credit_score >= 700:
    interest_rate = 3.5
elif credit_score >= 600:
    interest_rate = 5.5
else:
    interest_rate = 0.0

# Check approval criteria
if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount:
    approval_status = "Approved"
else:
    approval_status = "Rejected"
    interest_rate = 0.0  # No interest for rejected loans

print(interest_rate)
print(max_loan_amount)
print(approval_status)