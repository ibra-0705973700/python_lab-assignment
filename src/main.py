from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    name = input("Enter your name: ")
    print(greet(name))
    
    try:
        user_input = float(input("\nEnter a number: "))
        print(f"Square: {square(user_input)}")
        print(f"Is Even: {is_even(user_input)}")
        print(f"Fahrenheit Equivalent: {celsius_to_fahrenheit(user_input):.2f}°F")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
