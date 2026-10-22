def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("=== Python Calculator v2 ===")
    print("Operations: +, -, *, /")

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))

        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }

        if operator not in operations:
            print("Error: Invalid operator")
            return

        result = operations[operator](a, b)
        print(f"Result: {result:g}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    
    main()