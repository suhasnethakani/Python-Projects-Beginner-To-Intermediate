''' The Number Pattern We are about to print
                1
               222
              33333
             4444444
            555555555                  '''

try:
    n = int(input("Enter the number: "))
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        numbers = f"{i}" * (2 * i - 1)
        print(spaces + numbers)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
