def iseven(n):
    if n ^1 == n + 1:
        return True
    else:
        return False
    
number = int(input("Enter a number : "))

if iseven(number):
    print(f"The number '{number}'' is even.")
    
else:
    print(f"The number '{number}' is odd.")