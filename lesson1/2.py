# calculator

number1 = int(input("Enter numder: "))
symbol = input("Enter action: ")
number2 = int(input("Enter numder: "))
     
result = 0
     
if symbol == "+":
    	result = number1 + number2
elif symbol == "-":
    	result = number1 - number2
elif symbol == "*":
    	result = number1 * number2
elif symbol == "/":	
    	result = number1 / number2
     
print (result)
       