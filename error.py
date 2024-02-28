import os

try:
    x = int(input('Number should interget: '))
except ValueError:
    print('Invalid Input')
else:
    print(f'Integer: {x} + 1 = {x + 1}')


try:
    if 5 > 1:
        raise Exception('Hey Error')
except Exception as error:
    print(error)
finally:
    print('We are done')


