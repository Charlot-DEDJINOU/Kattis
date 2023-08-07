votes = {}
while True:
    s = input()
    if s == "***":
        break
    else:
        if s in votes:
            votes[s] += 1
        else:
            votes[s] = 1

max_votes = max(votes.values())
winners = [key for key, value in votes.items() if value == max_votes]

if len(winners) == 1:
    print(winners[0])
else:
    print("Runoff!")
