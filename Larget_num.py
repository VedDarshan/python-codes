n1, n2, n3 = map(int, input("Enter 3 values: ").split())
if (n1 >= n2) and (n1 >= n3):
    print(n1, "is largest number")
elif (n2 >= n1) and (n2 >= n3):
    print(n2, "is largest number")
else:
    print(n3, "is the larget")