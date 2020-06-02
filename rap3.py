
#PROBLEM-3:
"""
Given an object/dictionary, containing names as keys and amount_paid by each of them as
values, write a function that takes such an object as input and calculates the total sum paid by them together.

Below is an example:

Input: {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
Output: 275 """

#PROGRAM:

n=int(input("enter the value of n:\n"))
d={}
s=[]
for i in range(n):
    print("enter the ",i+1,"th key")
    key=input()
    print("enter the ",i+1,"th value")
    value=int(input())
    d[key]=value
s=sum(d.values())
print(d)
print("sum of values =",s)


#TESTED INPUTS AND OBTAINED OUTPUTS:
#INPUT-1:
"""enter the value of n:
5
enter the  1 th key
RICH
enter the  1 th value
85
enter the  2 th key
AMIT
enter the  2 th value
42
enter the  3 th key
GEORGE
enter the  3 th value
53
enter the  4 th key
TANYA
enter the  4 th value
60
enter the  5 th key
LINDA
enter the  5 th value
35
{'RICH': 85, 'AMIT': 42, 'GEORGE': 53, 'TANYA': 60, 'LINDA': 35}
sum of values = 275
>>> """
#INPUT-2:
'''
enter the value of n:
6
enter the  1 th key
ROSES
enter the  1 th value
20
enter the  2 th key
LOTUS
enter the  2 th value
0
enter the  3 th key
LILLIES
enter the  3 th value
3
enter the  4 th key
JASMIN
enter the  4 th value
1000
enter the  5 th key
SUNFLOWER
enter the  5 th value
234
enter the  6 th key
MARIGOLD
enter the  6 th value
1
{'ROSES': 20, 'LOTUS': 0, 'LILLIES': 3, 'JASMIN': 1000, 'SUNFLOWER': 234, 'MARIGOLD': 1}
sum of values = 1258
>>> 
'''

