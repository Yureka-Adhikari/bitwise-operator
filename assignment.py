a = int(input("Enter the first  number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def circuit(a, b, c):
    return (a & b) | (b | c) & (b & c)
    
print(f"The result of the circuit with inputs {a}, {b}, and {c} is: {circuit(a, b, c)}")