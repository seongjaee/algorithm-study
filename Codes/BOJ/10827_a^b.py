from decimal import *

getcontext().prec = MAX_PREC
a, b = input().split()
a = Decimal(a)
b = Decimal(b)
print(f'{a ** b:f}')
