num = int(input("Enter a number: "))

if num > 1:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")
else:
    print(num, "is not a Prime Number")