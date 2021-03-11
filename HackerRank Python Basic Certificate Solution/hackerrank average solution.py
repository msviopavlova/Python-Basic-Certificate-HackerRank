from decimal import *

def avg(*args):
    if len(args) == 1:
        for i in args:
            floated_number = float(i)
            getcontext().prec=2
            return Decimal(floated_number)
    else:
        average = sum(args) / len(args)
        average_float = float(average)
        getcontext().prec = 2
        return Decimal(average_float)






