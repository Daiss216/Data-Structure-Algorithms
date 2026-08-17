#Swaps two numbers using bitwise XOR without a third variable.
def bitwise_swap(num1,num2):

    num1= num1^num2
    num2= num1^num2
    num1= num1^num2

    return num1,num2

"""
## example:
x = 3
y = 7
print(f"original: num1= {x} , num2= {y}")

x,y= bitwise_swap(x,y)

print(f"Swapped: num1= {x} , num2= {y}")
"""