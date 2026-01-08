#basic calculator - DAY 1

#defining operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2
#number input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Mod")
print("6. Power")

#input for operation
choice = input("Enter choice(1/2/3/4): ")

#case statement
match choice:
    case '1':
        print(f"the result is {num1} + {num2} = ",add(num1, num2))
    case '2':
        print(f"the result is {num1} + {num2} = ",subtract(num1, num2))
    case '3':
        print(f"the result is {num1} + {num2} = ",multiply(num1, num2) )
    case '4':
        print(f"the result is {num1} + {num2} = ",divide(num1, num2))
    case '5':
        print(f"the result is {num1} + {num2} = ",mod(num1, num2))
    case '6':
        print(f"the result is {num1} + {num2} = ",power(num1, num2))
    case _:
        print(f"the result is {num1} + {num2} = ","Invalid input")