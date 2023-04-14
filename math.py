def add(a,b):
    answer=a+b
    return answer


def subtraction(c,d):
    answer=c-d
    return answer

def multiplication(e,f):
    answer=e*f
    return answer

def division(g,h):
    answer=g/h
    return answer

def remainder(i,j):
    answer=i%j
    return answer


def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total

def several_integers(*integers):
    total_multiplication=1
    for integer in integers:
        total_multiplication+= integer*integer
    return total_multiplication