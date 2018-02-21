# The user enters the number n. Then add N numbers.
# The program outputs the average of all numb.

num = int(input("Numbers count: "))
total = 0

for a in range(num):
    numbers = float(input("Enter number: "))
    total += numbers
avg = total/num
print("averege is:", avg)
