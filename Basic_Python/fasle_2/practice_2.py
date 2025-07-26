n = int(input())

if n < 2:
    print("not prime")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    print('prime') if is_prime else print('not prime')