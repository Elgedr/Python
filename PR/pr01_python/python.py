name = input('what is your name? ')
age = int(input(f' Hello, {name}. What year were you born in? '))

if age < 2008:
    print(f'You were {2008 - age} years old when Python 3.0 was released')
else: print(f'Python 3 was {age - 2008 } years old when you were born.')
