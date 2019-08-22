# def(*args):
#     return sum(args/len(args)

########
# def abs(num):
#     if num<0:
#        return -num
#     return num

########

# def rec(a,b):
#     return a*b
# def trg(a,b):
#     return 0.5*a*b
# def sq_circle(r):
#     return r**2*3.14

#     choice = input("1-rectangle, 2-triangle, 3-circle: ")
# if choice == '1':
#   rec(a=float(input('a:')),b=float(input('b:')))
# elif choice == '2':
#   trg(a=float(input('side:')),b=float(input('height:')))
# elif choice == '3':
#   cic(r=float(input('radius:'))
# else:
#   print("Input error")
########

# def count_sum(num):
#     sum=0
#     for i in str(num):
#         sum+=int(i)
#     return sum

#########
def addition(*args):
    return(sum(args))
def substraction(*args):
    res=0
    for i in args:
        res-=i
    return res
def multiplication(*args):
    res=1
    for i in args:
        res*=i
    return res
def division(*args):
    res=1
    for i in args:
        res/=i
    return res
def num_input():
    values=input('Please enter numbers with space separation')
    list_of_val=[int(i) for i in values.split()]
    return list_of_val

calc={'+':addition(), '-':substraction(), '*':multiplication(), '/':division()}

com=input('Enter "continue" or "exit"')
while com != 'exit':

    list_of_values=num_input()
    inp_opr=input("Now please enter the operation to compute: ")
    if inp_opr == '+':
        print(calc['+'],*list_of_values)
    elif inp_opr == '-':
        print(calc['-'],*list_of_values)
    elif inp_opr == '*':
        print(calc['*'],*list_of_values)
    elif inp_opr == '/':
        print(calc['/'],*list_of_values)
    else: print('Error. Please get acquainted with the instruction')
    com=input('Enter "continue" or "exit"')
    
else: print('Thank you for choosing our product')


########

# def fib(lim):
#     res=[]
#     a=1
#     b=1
#     while b < lim:
#         res.append(b)
#         a=b
#         b=a+b
#     return res

###########

# def discriminant(a,b,c):
#     return b**2 - 4*a*c