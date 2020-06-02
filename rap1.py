#PROBLEM-1:
'''
Write a program that prints the numbers from 1 to N. 
But, for multiples of three,  print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.

Below is an example:

Input: N = 17
Output:
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17'''


#PROGRAM
n=int(input("ENTER THE VALUE OF n\n"))
for i in range (1,n+1):
    if i%15==0:
        print("FizzBuzz",end=",")
    elif(i%3==0):
        print("Fizz",end=",")
    elif(i%5==0):
        print("Buzz",end=",")
    elif(i==n):
        print(i)
    else:
        print(i,end=",")
        

        
#TESTED INPUTS AND OBTAINED OUTPUTS:
#INPUT:1
"""
ENTER THE VALUE OF n
17
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17
>>>"""
#INPUT:2
"""
ENTER THE VALUE OF n
31
1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31
>>> 
"""
 
   
