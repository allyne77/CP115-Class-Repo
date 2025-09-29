num_days = int(input())
danger_threshold = float(input())

danger_days = 0
total_temperature = 0.0
days_processed = 0

for num in range(num_days):
    temp_reading = float(input())
                            
    total_temperature += danger_threshold
    days_processed += 1
    if temp_reading > danger_threshold:
        danger_days += 1
    else:
        if temp_reading <= danger_threshold:


        


# TODO: Your code here
# Use input() inside the loop to get each day's temperature

print(danger_days)
print(f"{average_temp:.1f}")