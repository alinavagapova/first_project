name = input('Enter your name:')
surname = input('Enter your surname:')
age = int(input('Enter your age:'))
print(age, type(age))
print('Hello, your name is {user_name}, your surname is {surname}, your age is {user_age}'.format(user_name=name, surname=surname, user_age=age))

