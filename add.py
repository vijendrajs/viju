def get_negative_numbers(numbers):
    negative_numbers = [number for number in numbers if number < 0]
    if negative_numbers:
        raise Exception('negative numbers not allowed', ', '.join(map(str, negative_numbers)))

def skip_large_numbers(numbers):
    numbers = [number for number in numbers if number <= 1000]
    return numbers



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

        #Raise Exceptions for negetive numbers
        get_negative_numbers(numbersList)

        #Skip numbers having values > 1000
        numbersList = skip_large_numbers(numbersList)

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

#Case: in case of negetive numbers raise exception
try:
    result = add('//;;\n1;;2;;,3\n-3, -2')
    print('result', result)
except Exception as e:
    print(e)

#Case: Skip numbers having values > 1000
result = add('//;;\n1,2,3\n3,1001, 1')
print('result', result)
