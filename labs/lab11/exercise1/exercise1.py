num_rounds = int(input())
score = int(input())

final_score = 0.0
rounds_processed = 0

for i in range(num_rounds):
    final_score += score
    rounds_processed += 1
    round_score = int(input())

    if _score <= 100:
        score_to_add = num_score * 1.20

        final_score += score_to_add


# TODO: Your code here
# Use input() inside the loop to get each round's score

print(f"{final_score:.1f}")
print(rounds_processed)