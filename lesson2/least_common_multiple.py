# Output the least common multiple of two numbers entered from the keyboard.

number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

def lcm(num_1, num_2): 
	if num_1 < num_2: 
		num_1 , num_2 = num_2, num_1 
	i=1 
	while (num_1 * i )% num_2 != 0: 
		i +=1 
	return num_1 * i 

print(LCM(number1, number2))
