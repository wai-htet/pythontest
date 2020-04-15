# finding the largest number
h = 56
g = 35
i = 78

if h > g:
    if h > i:
        print("h is the largest")
    elif g > i:
        print("g is the largest")
    else:
        print("i is the largest")

# finding the prime number

print("type a number and find out")

n = int(input())

if n % 2 == 0:
    print(n, 'is not a prime number')
else:
    print(n, 'is a prime number')
