correct_password = "python123"
login_successful = False
attempt = 0

while attempt < 3:
    entered_password = input("Enter your password: ")
    attempt += 1

    if entered_password == correct_password:
        login_successful = True
        break
    print("Incorrect password. Try again.")

# TODO: Your code here

print(login_successful)
print(attempt)
