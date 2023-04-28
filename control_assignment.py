#  Question one :Write a function that uses while, 
#  if and continue statements to print all the even numbers between 0 and 50.
def even_nums():
    nums=range(0,50)
    for num in nums:
        if num%2==0:
            print(num)


# Write a function that takes an integer argument and prints "Prime" if the number is prime,
#  and "Not prime" if the number is not prime.  

def is_num_prime(numbs):
    if numbs>1:
        for i in range(2,numbs):
            if(numbs%1)==0:
                print(f"{numbs} is not a prime")
                break
            else:
                print(f"{numbs} is prime")
            
        else:
                print(f"{numbs} is not prime")


#  Write a function that takes a list of integers as input 
#  and prints the sum of all the even numbers in the list
def even_sum(my_list):
    total=0
    for n in my_list:
        if n%2==0:
            total+=n
    print(total)



# Write a function that takes any two integers as input, and prints the sum of all the numbers
#  between the two integers (inclusive) that are divisible by 3.

def sum_numbers(x,y):
    total_nums=0
    for i in range(x,y+1):
        if i%3==0:
            total_nums+=i
    print(total_nums)


    
