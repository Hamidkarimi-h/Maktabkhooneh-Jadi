def count_divisors(n):
    count = 1
    i = 2
    while i * i <= n:
        power = 0
        while n % i == 0:
            n //= i
            power += 1
        count *= (power + 1)
        i += 1
    if n > 1:
        count *= 2
    return count

numbers = [int(input()) for _ in range(20)]

max_div_count = -1
number_with_max_div = -1

for num in numbers:
    div_count = count_divisors(num)
    if div_count > max_div_count or (div_count == max_div_count and num > number_with_max_div):
        max_div_count = div_count
        number_with_max_div = num

print(number_with_max_div, max_div_count)
