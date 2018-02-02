# The user enters the number n. Then add N numbers. The program outputs the average of all numb
	
num = int(input("Numbers count: "))
sum = 0

for a in range(num):
	numbers = float(input("Enter number: "))
	sum += numbers
avg = sum/num
print("averege is:", avg)
