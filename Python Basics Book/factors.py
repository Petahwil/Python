n = input('Enter a positive integer: ')
x = int(n)
while x > 0:
    if (int(n)%x) == 0:
        print(f'{x} is a factor of {n}')
    x-=1