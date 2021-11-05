# My try
n = input('Enter a positive integer: ')
x = int(n)
while x > 0:
    if (int(n)%x) == 0:
        print(f'{x} is a factor of {n}')
    x-=1
    
# Ans have to get a better understaning of if statments. 
# I wanted to use one for this but dont understand them enough.
# The book hasn't giving a good explination of them
num = int(input("Enter a positive integer: "))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(f"{divisor} is a factor of {num}")