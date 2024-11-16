# Adding 2 numbers but not accepting negative integer
def main():
    a = float(input("Enter a number: "))
    b = float(input("Enter a number: "))
    sum = a + b
    while (a < 0) or (b < 0):
        print("Entre positive integer")
        break
    else:
        print("Sum of given numbers", sum)

main()
