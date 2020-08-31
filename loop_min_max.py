intLargest = None
intSmallest = None

while True:
    strVal = input('Enter a number: ')
    if strVal == 'done':
        break

    try:
        intVal = int(strVal)
        if intLargest is None:
            intLargest = intVal
            intSmallest = intVal
        elif intVal > intLargest:
            intLargest = intVal
        elif intVal < intSmallest:
            intSmallest = intVal

    except ValueError:
        print('Invalid input')
        continue


print('Maximum is', intLargest)
print('Minimum is', intSmallest)