# TODO: Your code here
target1 = 7
target2 = 13
found_number = False

for number in range(20):
    print(f'Checking number: {number}')
    if number == target1 or number == target2:
       found_number = True
       print(f'Found target number: {number}')
       continue

print(found_number)
