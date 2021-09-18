def fizzbuzz(num):
    print (num)
    if (num % 15 == 0):
        print ("FizzBuzz")
    elif (num % 5 == 0):
        print ("Buzz")
    elif (num % 3 == 0):
        print ("Fizz")
    else:
        print ("Number is divisible by neither 3 nor 5")

numbers = [3,5,15,17,25,27,30,47,51,77,80,85,90,100,150]

for num in numbers:
    fizzbuzz(num)
