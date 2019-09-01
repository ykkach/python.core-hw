try:
    def odd(num):
        if num%2 == 0:
            return 'Your number is odd'
        return 'Your number is even'
    num = int(input('Enter a number'))
    print(odd(num))
except ValueError:
    print('Valueerror! Str is inappropriate type')

###################################################

# 1
n = input("Input entire number: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("\n You entered incorrect data!\n")
        n = input("Input entire number:\n ")
 
if n % 2 == 0:
    print("{0} is the even number.".format(n))
else:
    print("{0} is the odd number.".format(n))

##################################################

def enterage(age):
    if age <= 0:
        raise ValueError
    if age%2 == 0:
        print('age is even')
    else:
        print('age is odd')
try:
    age = int(input('Write your age'))
    enterage(age)
except ValueError:
    age = input('Invalid input. Please enter a positive number:')
print('Your age is {0}' .format(age))

###################################################
# 1
def division(prompt = '')
    try:
        n = list(input(prompt).split(,))
            div = d[0]/d[1]
    except ZeroDivisionError:
        print('Error, division by zero')

##########################################################
# 2
try:
    num1, num2 = eval(input('enter two numbers, separated by a coma'))
    res = num1/num2
    print('resul is ', res)
except ZeroDivisionError:
     print('Division by zero is error')
except SybtaxError:
    print("Error. Coma is missing")
except ValueError:
    print("Value Error")


day_of_the_week = {1:'monday',2: 'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'Saturday', 7:'Sunday'}
while True:
    try:
        i = int(input('Enter a number of the day of the week'))
    except ValueError:
        print('str is an appropriate type')
    else:
        if i not in range(6):
            raise IndexError("The number is incorrect")
        # print(day_of_the_week.get(i, 'There is no such a day of the week'))
    


