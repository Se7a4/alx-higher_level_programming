#!/usr/bin/python3
import calculator_1
import sys
if __name__=="__main__":
    if len(sys.argv[1:]) != 3 :
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    var_oprator= sys.argv[2]
    b = int(sys.argv[3])
    if var_oprator != '+'and var_oprator !='-'and var_oprator !='*'and var_oprator !='/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    if var_oprator == '+':
        print(f"{a} + {b} = {calculator_1.add(a, b)}")
    elif var_oprator == '-':
        print(f"{a} - {b} = {calculator_1.sub(a, b)}")
    elif var_oprator == '*':
        print(f"{a} * {b} = {calculator_1.mul(a, b)}")
    elif var_oprator == '/':
        print(f"{a} / {b} = {calculator_1.div(a, b)}")
