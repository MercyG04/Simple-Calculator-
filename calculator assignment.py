import re
import math

def calculate(expression):
    # Replace '^' with '**' for exponentiation
    expression = expression.replace('^', '**')
    
    # Solve expressions inside parentheses
    while '(' in expression:
        innermost_expr = re.search(r'\(([^()]+)\)', expression)
        if innermost_expr:
            result = calculate(innermost_expr.group(1))
            expression = expression.replace(innermost_expr.group(0), str(result))
        else:
            break

    # Solve exponentiation
    while '**' in expression:
        exp_match = re.search(r'(\d+(\.\d+)?)\s*\*\*\s*(\d+(\.\d+)?)', expression)
        if exp_match:
            base = float(exp_match.group(1))
            exponent = float(exp_match.group(3))
            result = base ** exponent
            expression = expression.replace(exp_match.group(0), str(result))
        else:
            break

    # Solve multiplication and division
    mul_div_match = re.search(r'(\d+(\.\d+)?)\s*([*/])\s*(\d+(\.\d+)?)', expression)
    while mul_div_match:
        num1 = float(mul_div_match.group(1))
        operator = mul_div_match.group(3)
        num2 = float(mul_div_match.group(4))
        
        if operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        expression = expression.replace(mul_div_match.group(0), str(result))
        mul_div_match = re.search(r'(\d+(\.\d+)?)\s*([*/])\s*(\d+(\.\d+)?)', expression)

    # Solve addition and subtraction
    add_sub_match = re.search(r'(\d+(\.\d+)?)\s*([+\-])\s*(\d+(\.\d+)?)', expression)
    while add_sub_match:
        num1 = float(add_sub_match.group(1))
        operator = add_sub_match.group(3)
        num2 = float(add_sub_match.group(4))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2

        expression = expression.replace(add_sub_match.group(0), str(result))
        add_sub_match = re.search(r'(\d+(\.\d+)?)\s*([+\-])\s*(\d+(\.\d+)?)', expression)

    try:
        result = float(expression)
        return result
    except ValueError:
        return "Error: Invalid Expression"

def main():
    print("Welcome to my Calculator!")
    expression = input("Enter an expression: ")
    result = calculate(expression)
    print("Result:", result)

if __name__ == "__main__":
    main()
