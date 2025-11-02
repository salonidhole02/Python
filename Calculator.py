num1 = float(input("Enter your first number : "))
operator =input("Enter your Operator(+, -, *, /): ")
num2 = float(input("Enter your second number:"))
if operator == '+':
    result = num1 + num2 
    print('result:', result)
    
elif operator == '-':
    result =num1 - num2
    print('result:', result)
    
elif operator == '*':
    result =num1 * num2
    print('result:', result)
    
elif operator == '/':
    if num2 !=0:
        result = num1 / num2
        print('result:', result)
    else:
        print("ERROR")
else:
    print("Invalid Character")