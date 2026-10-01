""" print(f"Give me your first number of the equation.")

x1 = input()

print(f"Okay now the second number please.")

y1 = input()

#test for variable numbers
#print(f"{x} and {y}")

#Operator selector 

print(f"What symbol are you using?")

op = input()

if op == "x":
    print(int(x1) * int(y1))

elif op == "+":
    print(int(x1) + int(y1))
    
elif op == "-":
    print(int(x1) - int(y1))
    
elif op == "/":
    print(int(x1) / int(y1))
    
elif op == "%":
    print(int(x1) % int(y1)) """
    
def calculate(x, op, y):
    if op == "x":
        return int(x) * int(y)
    elif op == "+":
        return int(x) + int(y)
    elif op == "-":
        return int(x) - int(y)
    elif op == "/":
        return int(x) / int(y)
    elif op == "%":
        return int(x) % int(y)
    else:
        return "Invalid operator"
    

print(calculate(100, "x", 4000))