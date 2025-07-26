low, high = 1, 99

while low <= high:
    guess = (low + high) // 2
    print(guess)

    ans = input()
    if ans == 'd':
        print('bravo...')
        break
    
    elif ans == 'k':
        high = guess - 1
    elif ans == 'b':
        
        low = guess + 1
    else:
        print('Invalid input ...')




