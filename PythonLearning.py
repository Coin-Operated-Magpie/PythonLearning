numbers = range(10)
previous_number = numbers[0]
for index,current_number in enumerate(numbers):
    if current_number > 0:
        previous_number = current_number - 1
    print("Current Number "+str(current_number)+" Previous Number "+str(previous_number)+" Sum "+str(current_number+previous_number))