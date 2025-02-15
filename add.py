def add(numbers=''):
    numbers = str(numbers)
    if not numbers:
        return 0
    
    mainDelimeter = ','
    if '//' in numbers:
        # Find the positions of the delimiters
        end_index = numbers.find('\n')
        mainDelimeter = numbers[2:end_index]
        numbers = numbers.replace('//', '')

    delimeterList = [',', '\n', '?']
    delimeterList.append(mainDelimeter)
    if any(delimiter in numbers for delimiter in delimeterList):
        for delimiter in delimeterList:
            numbers = numbers.replace(delimiter, ',')
        numbersList = [int(num) for num in numbers.split(',') if num]
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

#Dynamic delimeter at starting in string - //;\n
result = add('//;\n1;2')
print('result', result)
result = add('//;;\n1;;2')
print('result', result)
result = add('//;;\n1;;2;;,3\n3')
print('result', result)
