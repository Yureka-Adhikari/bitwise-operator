def numofbits(n):
    count = 0
    while(n):
        count += 1
        n>>= 1
    return count

number = int(input("Enter a number : "))
print(f"The number of bits in {number} is {numofbits(number)}")