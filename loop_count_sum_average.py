intNum = 0
fltTotal = 0.0

while True:
    strVal = input('Enter a number: ')
    if strVal == 'done':
        break

    try:
        fltVal = float(strVal)
        intNum += 1
        fltTotal += fltVal
    except ValueError:
        print('Invalid Input value, continuing...')
        continue


print("The number of valid lines:{}, the total:{}, the average:{}".format(intNum, fltTotal, fltTotal / intNum))
