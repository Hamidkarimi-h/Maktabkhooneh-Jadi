total_points = 0
wins = 0

for _ in range(30):
    point = int(input())
    total_points += point
    if point == 3:
        wins += 1

print(total_points, wins)