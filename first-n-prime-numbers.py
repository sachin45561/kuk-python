# Write a program to find first n prime numbers

n = int(input("Enter how many prime numbers you want: "))

count = 0
num = 2

while count < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1

    