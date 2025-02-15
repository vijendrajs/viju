#Case 1: Test Code for empty string and "1" string and numeric 1 string.

def add(numbers=''):
    numbers = str(numbers)
    if not numbers:
        return 0
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
