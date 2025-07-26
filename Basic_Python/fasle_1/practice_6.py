age = int(input())
if 0 < age < 6:
    print('khordsal')
elif 6 <= age < 10:
    print('koodak')  
elif 10 <= age < 14:
    print('nojavan')
elif 14 <= age < 24:
    print('javan')
elif 24 <= age < 40:
    print('bozorgsal')
elif 40 <= age:
    print('miansal')

# ------------------------------------

age = int(input())

age_ranges = [
    ((0, 6), "khordsal"),
    ((6, 10), "koodak"),
    ((10, 14), "nojavan"),
    ((14, 24), "javan"),
    ((24, 40), "bozorgsal"),
    ((40, float('inf')), "miansal"),
]

output = 'Invalid input'

for (start, end), label in age_ranges:
    if start < age < end or (start <= age < end):
        output = label
        break

print(output)