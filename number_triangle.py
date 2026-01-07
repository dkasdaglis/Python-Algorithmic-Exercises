# Project: Number Triangle Generator
# Description: Prints a triangle of digits based on user input.

print("--- Number Triangle Generator ---")

while True:
    # Get input from user
    try:
        n = int(input("Enter a number (1-9) or 0 to exit: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Check exit condition
    if n == 0:
        print("Exiting program...")
        break
    
    # Check valid range and print pattern
    elif 1 <= n <= 9:
        for i in range(n, 0, -1):
            print(str(n) * i)
    else:
        print("Number must be between 1 and 9.")
        continue
