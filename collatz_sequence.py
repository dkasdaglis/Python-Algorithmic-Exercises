# Project: Collatz Conjecture (3n + 1 problem)
# Description: Calculates the sequence steps for a given number and finds the number with max steps in a range.

def calculate_collatz_steps(n):
    """Calculates the number of steps to reach 1."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# --- Part A: User Input ---
print("\n--- Part A: Calculate Steps for a Number ---")
while True:
    try:
        user_n = int(input("Enter a number (2-10000): "))
        if 2 <= user_n <= 10000:
            break
        print("Please enter a number within the range.")
    except ValueError:
        print("Invalid input.")

steps_taken = calculate_collatz_steps(user_n)
print(f"Number {user_n} reached 1 in {steps_taken} steps.")

# --- Part B: Find Max Steps in Range ---
print("\n--- Part B: Analyzing Range 2-10000 ---")
max_steps = 0
best_n = 0

for n in range(2, 10001):
    current_steps = calculate_collatz_steps(n)
    
    if current_steps > max_steps:
        max_steps = current_steps
        best_n = n

print(f"Result: The number {best_n} produces the longest chain ({max_steps} steps).")
