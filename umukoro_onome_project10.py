import art_project10

print(art_project10.logo)
def add(n1, n2):
    return n1 + n2

my_favorite_operation = add
# print(my_favorite_operation(n1=2, n2=3))

# TODO: Write ouf the other 3 functions - subtract, multiply * and divide %
def subtract(n1, n2):
    return n1 - n2
result = subtract
# print(subtract(n1=2, n2=3))

def multiply(n1, n2):
    return n1 * n2
# print(multiply(n1=2, n2=3))

def divide(n1, n2):
    return n1 / n2
# print(divide(n1=2, n2=3))

# TODO: Add these four functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dic. operations to perform the calculations, multiply 4 by 8 using the dictionary.

# print(Operations["*"](4,8))
def calculator():

  should_accumulate = True
  num1 = float(input("What's the first number?: "))

  while should_accumulate:
      for symbol in operations:
       print(symbol)
       operation_symbol = input("Input an operator: ")
       num2 = float(input("Input the second number: "))
       answer = operations[operation_symbol](num1 , num2)
       print(f"{num1} {operation_symbol} {num2} = {answer}")

       choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

       if choice == "y":
          num1 = answer
       else:
           should_accumulate = False
           print("\n" * 20 )
           calculator()

calculator()


