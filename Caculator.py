#Ultimate Math caculator

#Imports
import math
import cmath
import time

#Main Menu
def main():
    print("Welcome to the Ultimate Math Calculator!")
    print("Please select a function")
    print("1. Algebra")
    print("2. Trigonometry")
    print("3. Calculus")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        algebra()
    elif choice == "2":
        trig()
    elif choice == "3":
        calc()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice")
        main()
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

main()