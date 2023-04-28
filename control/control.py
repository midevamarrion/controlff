# Write a function that uses while, if and continue statements to print 
# all the even numbers between 0 and 50. 
def even_numbers():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)
# Write a function that takes an integer argument and prints "Prime" if the
#  number is prime, and "Not prime" if the number is not prime.

def prime(n):
    if n <= 1:
        print("Not prime")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")




# Write a function that takes a list of integers as input and prints the 
# sum of all the even numbers in the list.

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print("The sum of all even numbers is:", total)
# Write a function that takes any two integers as input, and prints the sum
#  of all the numbers between the two integers (inclusive) that are 
# divisible by 3.
def sum_three(min, max):
    total = 0
    for num in range(min, max+1):
        if num % 3 == 0:
            total += num
    print("The sum is:", total)


