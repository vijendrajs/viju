class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def get_negative_numbers(numbers):
    """Check for negative numbers and raise an exception if found."""
    negative_numbers = [number for number in numbers if number < 0]
    if negative_numbers:
        raise NegativeNumberError('negative numbers not allowed', ', '.join(map(str, negative_numbers)))

def skip_large_numbers(numbers):
    """Return a list of numbers that are less than or equal to 1000."""
    return [number for number in numbers if number <= 1000]

def parse_delimiters(numbers: str) -> tuple:
    """Parse custom delimiters from the input string."""
    main_delimiter = ','
    if '//' in numbers:
        end_index = numbers.find('\n')
        main_delimiter = numbers[2:end_index]
        numbers = numbers[end_index + 1:]
    return main_delimiter

def add(numbers=''):
    numbers = str(numbers)
    if not numbers:
        return 0
    
    mainDelimeter = parse_delimiters(numbers)
    numbers = numbers.replace('//', '')
    delimeterList = [',', '\n', '?', mainDelimeter]

    for delimiter in delimeterList:
        numbers = numbers.replace(delimiter, ',')
    numbersList = [int(num) for num in numbers.split(',') if num]

    #Raise Exceptions for negetive numbers
    get_negative_numbers(numbersList)

    #Skip numbers having values > 1000
    numbersList = skip_large_numbers(numbersList)

    numbersList = list(map(int, numbersList))
    return sum(numbersList)

#Case: Empty String
result = add("")
print('result A - ', result)

#Case: Single Number in string format
result = add('1')
print('result B - ', result)

#Case: Single Number in numeric format
result = add(1)
print('result C - ', result)

#Case: multiple Number
result = add('1,2')
print('result D - ', result)
result = add('1,2,5,6')
print('result E - ', result)

#Case: comma and \n as delimeter
result = add('1\n2,5,6')
print('result F - ', result)
result = add('1\n2,3,4\n5,6')
print('result I - ', result)

#Case: [',', '\n', '?'] as delimeter
result = add('1\n2,3,4\n5?6')
print('result G -', result)
result = add('1\n2,3,4\n5?6?7')
print('result H - ', result)

#Dynamic delimeter at starting in string - //;\n
result = add('//;\n1;2')
print('result I - ', result)
result = add('//;;\n1;;2')
print('result J -', result)
result = add('//;;\n1;;2;;,3\n3')
print('result K -', result)

#Case: in case of negetive numbers raise exception
try:
    result = add('//;;\n1;;2;;,3\n-3, -2')
    print('result L -', result)
except NegativeNumberError as e:
    print(e)

#Case: Skip numbers having values > 1000
result = add('//;;\n1,2,3\n3,1001, 1')
print('result M - ', result)

#delimeter can be of any lenght '###' and multiple delimeters, just add the delimeters in delimeterList object.
result = add('//###\n1###2###,,3\n3,1001, 1')
print('result N -', result)
