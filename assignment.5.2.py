largest = None
smallest = None

while True:
	num = input("Enter a number: ")
	if num == "done":
		break
	try:
		number = int(num)
		if smallest is None:
			smallest = largest = number
		elif number < smallest:
			smallest = number
		elif number > largest:
			largest = number
	except:
		print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
