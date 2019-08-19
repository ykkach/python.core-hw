num=input('enter your 4 digits number:' )
mult = 1
for i in num:
    if int(i) != 0:
        mult *= int(i)
print(mult, 'is the result of multiplication')

for a in reversed(num):
    print(a, end='')

print(sorted(num),'is your sorted number')