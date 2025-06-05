def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

try:
    print("Temperature Converter")
    temp = float(input("Enter the temperature value: "))
    
    print("\nChoose conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        result = celsius_to_fahrenheit(temp)
        print(f"\n{temp}°C is {result:.2f}°F")
    elif choice == 2:
        result = fahrenheit_to_celsius(temp)
        print(f"\n{temp}°F is {result:.2f}°C")
    else:
        print(" Invalid choice. Please enter 1 or 2.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
