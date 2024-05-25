n = int (input("Enter number: "))
if n == 1:
    print ("it's not prime")
if n > 1:
    for i in range (2,n-1):
        if n % i == 0:
            print (" It's not prime number")
            break
    else:
        print("It's the prime")