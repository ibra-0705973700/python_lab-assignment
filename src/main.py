from utils import square, is_even, celsius_to_fahrenheit

def main():
    user_input = input("Geli nambar: ")
    n = float(user_input)
    
    print(f"Square: {square(n)}")
    print(f"Is Even: {is_even(n)}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(n)}")

if __name__ == "__main__":
    main()
