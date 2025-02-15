def add(numbers=''):
    numbers = str(numbers)
    if not numbers:
        return 0
  
    delimeter = ','
    delimeter2 = '\n'
    if delimeter in numbers:
        numbers = numbers.replace(delimeter2, ',')
        numbersList = numbers.split(delimeter)
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
