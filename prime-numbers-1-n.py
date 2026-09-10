## write a program to print all prime numbers between 1 and 100

n = 100
for num in range(2, n + 1):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    else:
        print(num, end=" ")