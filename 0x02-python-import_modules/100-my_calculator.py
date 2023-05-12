#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1
    num_argument = len(sys.argv)
    argu_array = sys.argv
    operator_list = ['+', '-', '*', '/']
    if num_argument != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if str(argu_array[2]) not in operator_list:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(argu_array[1])
        b = int(argu_array[3])
        if str(argu_array[2]) == '+':
            print(f"{a} {argu_array[2]} {b} = {calculator_1.add(a, b)}")
        elif str(argu_array[2]) == '-':
            print(f"{a} {argu_array[2]} {b} = {calculator_1.sub(a, b)}")
        elif str(argu_array[2]) == '*':
            print(f"{a} {argu_array[2]} {b} = {calculator_1.mul(a, b)}")
        elif str(argu_array[2]) == '/':
            print(f"{a} {argu_array[2]} {b} = {calculator_1.div(a, b)}")
