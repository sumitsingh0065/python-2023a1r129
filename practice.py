def greet_user(name):
    print(f"Hello, {name}! Welcome to Python practice.")

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print("=== Simple Python Practice ===")
    name = input("Enter your name: ")
    greet_user(name)

    numbers = []
    print("\nEnter 5 numbers:")
    for i in range(5):
        num = float(input(f"Number {i+1}: "))
        numbers.append(num)

    avg = calculate_average(numbers)
    print(f"\nThe average of your numbers is: {avg:.2f}")

    if avg > 50:
        print("That's a high average! Great job.")
    else:
        print("Keep practicing — you'll improve!")

    print("\n=== End of Program ===")

if __name__ == "__main__":
    main()
