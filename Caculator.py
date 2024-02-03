#Ultimate Math caculator

#Imports
 # This code imports the math and cmath modules, which provide mathematical functions and operations.
import math
import cmath
import time

#Main Menu
def main():
    """
    This is the main function of the Ultimate Math Calculator. It presents the user with a menu of options
    to choose from. The options include Algebra, Trigonometry, Calculus, and Exit. Depending on the user's
    choice, it calls the appropriate function. If the user enters an invalid choice, it prints an error message
    and calls itself again to present the menu to the user.
    """
    print("Welcome to the Ultimate Math Calculator!")  # Welcome message
    print("Please select a function")  # Prompt for the user to select a function
    print("1. Algebra")  # Option 1: Algebra
    print("2. Trigonometry")  # Option 2: Trigonometry
    print("3. Calculus")  # Option 3: Calculus
    print("4. Exit")  # Option 4: Exit the program
    choice = input("Enter your choice: ")  # Get the user's choice

    # Depending on the user's choice, call the appropriate function
    if choice == "1":
        algebra()  # Call the algebra function if the user chose option 1
    elif choice == "2":
        trig()  # Call the trigonometry function if the user chose option 2
    elif choice == "3":
        calc()  # Call the calculus function if the user chose option 3
    elif choice == "4":
        exit()  # Exit the program if the user chose option 4
    else:
        print("Invalid choice")  # Print an error message if the user entered an invalid choice
        main()  # Call itself again to present the menu to the user
#Algebra
def algebra():

    def factor_quadratic(a, b, c):
        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # If the discriminant is negative, the equation has no real roots
        if discriminant < 0:
            return "No real roots"

        # If the discriminant is zero, the equation has one real root
        elif discriminant == 0:
            root = -b / (2*a)
            return f"One real root: {root}"

        # If the discriminant is positive, the equation has two real roots
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"Two real roots: {root1}, {root2}"

    def factor_cubic(a, b, c, d):
        # Calculate the discriminant
        discriminant = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2

        # If the discriminant is zero, the equation has one real root
        if discriminant == 0:
            root = -b / (3*a)
            return f"One real root: {root}"

        # If the discriminant is positive, the equation has three real roots
        elif discriminant > 0:
            root1 = (-1/(3*a))*(b + cmath.sqrt(-discriminant) + cmath.sqrt(2*b**3 - 9*a*b*c + 27*a**2*d))
            root2 = (-1/(3*a))*(b - cmath.sqrt(-discriminant) + cmath.sqrt(2*b**3 - 9*a*b*c + 27*a**2*d))
            root3 = (-1/(3*a))*(b - cmath.sqrt(-discriminant) - cmath.sqrt(2*b**3 - 9*a*b*c + 27*a**2*d))
            return f"Three real roots: {root1}, {root2}, {root3}"

        # If the discriminant is negative, the equation has one real root and two complex roots
        else:
            root1 = (-1/(3*a))*(b + cmath.sqrt(-discriminant))
            root2 = (-1/(3*a))*(b - cmath.sqrt(-discriminant))
            return f"One real root and two complex roots: {root1}, {root2}"

    def ask_equation_type():
        print("Which type of equation do you want to solve?")
        print("1. Quadratic equation")
        print("2. Cubic equation")
        choice = input("Enter your choice: ")
        if choice == "":
            exit()
        return choice

    equation_type = ask_equation_type()

    if equation_type == "1":
        print("Enter the coefficients of a quadratic equation in the form ax^2 + bx + c = 0:")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        if a or b or c == "":
            exit()
        print(factor_quadratic(a, b, c))
    elif equation_type == "2":
        print("Enter the coefficients of a cubic equation in the form ax^3 + bx^2 + cx + d = 0:")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        d = float(input("d = "))
        if a or b or c or d == "":
            exit()
        print(factor_cubic(a, b, c, d))
    else:
        print("Invalid choice")

# Exponents and logarithms
def expo():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print(f"{base}^{exponent} = {base**exponent}")
def log():
    base = int(input("Enter the base: "))
    value = int(input("Enter the value: "))
    rounding = int(input("Enter the number of decimal places to round to (press enter none): "))
    if rounding == "":
        print(f"log_{base}({value}) = {math.log(value, base)}")
    else:
        print(f"log_{base}({value}) = {round(math.log(value, base), rounding)}")

#Factorials
def factorial():
    number = int(input("Enter a number: "))
    print(f"{number}! = {math.factorial(number)}")

#Permutations and combinations
def perm():
    n = int(input("Enter the number of items: "))
    r = int(input("Enter the number of items to choose: "))
    print(f"{n}P{r} = {math.perm(n, r)}")

def comb():
    n = int(input("Enter the number of items: "))
    r = int(input("Enter the number of items to choose: "))
    m = int(input("Enter the number of items that are duplicated: "))
    print(f"{n}C{r} = {math.comb(n, r)}/{m}! = {math.comb(n, r) / math.factorial(m)}")


#Trigonometry
def trig():
    def calculate_particular_solution(value, operation):
        if operation == 'sin':
            radian = math.asin(value)
            other_solution = lambda degree: 180 - degree
        elif operation == 'cos':
            radian = math.acos(value)
            other_solution = lambda degree: 360 - degree
        elif operation == 'tan':
            radian = math.atan(value)
            other_solution = lambda degree: 180 + degree
        elif operation == 'cot':
            radian = math.atan(1/value) if value != 0 else None
            other_solution = lambda degree: 180 + degree
        elif operation == 'sec':
            radian = math.acos(1/value) if value != 0 else None
            other_solution = lambda degree: 360 - degree
        elif operation == 'csc':
            radian = math.asin(1/value) if value != 0 else None
            other_solution = lambda degree: 180 - degree
        else:
            return "Invalid operation"

        if radian is None:
            return "Undefined"

        # Convert the result to degrees
        degree = math.degrees(radian)

        # If the degree is negative, add 360 to get the equivalent positive angle
        if degree < 0:
            degree += 360

        # Calculate the other solution

        degree2 = other_solution(degree)
        print(degree)
        print(degree2)
        if degree2 < 0:
            degree2 += 360
        elif degree2 >= 360:
            degree2 -= 360

        return degree, degree2

    # Test the function

    while True:
        operation = input("Enter the operation (sin, cos, tan, cot, sec, csc) or press Enter to exit: ")
        if operation == "":
            break
        value = float(input("Enter the value of the operation: "))
        degree1, degree2 = calculate_particular_solution(value, operation)
        print(f"The particular solutions for {operation}={value} are {degree1} degrees and {degree2} degrees")

# Convertions
def convert():
    print("1. Degrees to radians")
    print("2. Radians to degrees")
    choice = input("Enter your choice: ")
    if choice == "1":
        degree = float(input("Enter the degree: "))
        print(f"{degree} degrees = {math.radians(degree)} radians")
    elif choice == "2":
        radian = float(input("Enter the radian: "))
        print(f"{radian} radians = {math.degrees(radian)} degrees")
    else:
        print("Invalid choice")

def convert_per_to_frac():
    percent = float(input("Enter the percentage: "))
    print(f"{percent}% = {percent/100}")

main()
