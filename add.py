def add(numbers=''):
    numbers = str(numbers)
    if not numbers:
        return 0
   
    mainDelimeter = ','
    delimeterList = [',', '\n', '?']
    if any(delimiter in numbers for delimiter in delimeterList):
        for delimiter in delimeterList:
            numbers = numbers.replace(delimiter, ',')
        numbersList = numbers.split(mainDelimeter)
        numbersList = list(map(int, numbersList))
        result = sum(numbersList)
        return result
    else:
        return numbers

#Case: Empty String
result = add("")
print('result', result)

#Case: Single Number in string format
result = add('1')
print('result', result)

#Case: Single Number in numeric format
result = add(1)
print('result', result)

#Case: multiple Number
result = add('1,2')
print('result', result)
result = add('1,2,5,6')
print('result', result)

#Case: comma and \n as delimeter
result = add('1\n2,5,6')
print('result', result)
result = add('1\n2,3,4\n5,6')
print('result', result)

#Case: [',', '\n', '?'] as delimeter
result = add('1\n2,3,4\n5?6')
print('result', result)
result = add('1\n2,3,4\n5?6?7')
print('result', result)
