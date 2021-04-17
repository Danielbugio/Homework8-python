print("type first number")
firstNumber = float(input())

print("type second number")
secondNumber = float (input())

print ("Which arithmetic operation you want to do: '+' , '-' ,  '*' or  '/'")
operation = input()

if operation == "+":
    print (firstNumber + secondNumber)  
elif operation == "-":
    print (firstNumber - secondNumber)
elif operation == "*":
    print (firstNumber * secondNumber) 
elif operation == "/":
    print (firstNumber / secondNumber)
else:
    print("I dont recognize this aritmetic operation")
