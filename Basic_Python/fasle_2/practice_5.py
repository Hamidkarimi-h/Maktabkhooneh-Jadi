max_age1 = -1
max_age2 = -1

while True:
    age = int(input())
    if age == -1:
        break
    if age > max_age1:
        max_age2 = max_age1
        max_age1 = age
    elif age > max_age2:
        max_age2 = age

print(max_age1, max_age2)

# -----------------------------------

ages = []

while True:
    age = int(input())
    if age == -1:
        break
    ages.append(age)

ages.sort(reverse=True)
print(ages[0], ages[1])