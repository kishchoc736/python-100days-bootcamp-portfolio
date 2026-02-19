import art


def add(n1, n2):
    return n1 + n2

my_fav_operation = add

# print(my_fav_operation(2,3))

# Write out 3 other functions

def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

# Add these 4 functions into a dictionary as the values: Keys = "+", ...

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Use the dictionary operations to perform the calculations. 4*8 using the dictionary

# print(operators["*"](4,8))

def my_calcualator():
    """ Opens a calculator that runs until user enters 'n' """
    print(art.logo)
    should_accumulate = True
    number_1 = int(input("Enter the first number: "))
    while should_accumulate:
        print("Select one of the following options:")
        for operator in operators:
            print(operator)
        operator = input("Enter the operator: ")
        number_2 = int(input("Enter the second number: "))
        result = operators[operator](number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {result}")
        keep_going = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if keep_going == "y":
            number_1 = result
        else:
            print("\n" * 20)
            my_calcualator()

my_calcualator()


