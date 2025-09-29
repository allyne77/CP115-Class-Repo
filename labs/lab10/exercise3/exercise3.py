monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())
interest_rate = 0.0
max_loan_amount = monthly_income * 5
approval_status = "Rejected" 

if credit_score >= 700:
    interest_rate = 3.5
elif credit_score >= 600:
    interest_rate = 5.5
else:
    interest_rate = 0.0

if (monthly_income >= 4000 and 
    credit_score >= 600 and 
    loan_amount <= max_loan_amount):
    
    approval_status = "Approved"
else:
    
    interest_rate = 0.0
    approval_status = "Rejected"  

# Output the results
print(interest_rate)
print(max_loan_amount)
print(approval_status)