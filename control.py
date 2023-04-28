def even_numbers(x=range(10)):
    for i in x:
        if(i%2==0):
            print(i)


def odd_numbers(x=range(10)):
    for i in x:
        if(i%2!=0):
            print(f"{i} is divisible by five")


def divisible_by_five():
    x=range(30)
    for i in x:
        if(i%5==0):
            print(i)
        else:
                print(f" {i} not divisible by 5")


def multiple_comparison():
    x=range(30)
    for i in x:
        if(i%2==0):
            print(f"{i} is divisible by 2")
        elif(i%3==0):
            print(f"{i} is divisible by 3")
        elif(i%5==0):
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 2,3 0r 5")


def divisible_by_two_and_three():
    x=range(30)
    for i in x:
        if(i%2==0 and i%3==0):
            print(f"{i} is divisible by 2 and 3")
        elif(i%2==0 or i%3==0):
            print(f"{i} is divisible by either 2 or 3")
        else:
            print(f"{i} is not divisible by 2 and 3")


def another():
    x=1
    while(x<10):
        print("Hello Akirachix")
        if(x==5):
            break
            x+=1

def break_statement():
    x=1
    while(x<10):
        x+1
        print("Hello AkiraChix")
        if(x==5):
            break 
        

def continue_statement():
    x=1
   
    while(x<10):
        x+=1
        if(x%2!=0):
            continue
        print(x)



        
