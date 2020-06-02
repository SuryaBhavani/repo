#PROBLEM-2:
"""
Given an array print all the numbers that are repeating in it and the number of times they are repeating.

Below is an example:

Input: [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
Output:
1 - 4
2 - 2
5 - 3
8 - 2
4 - 2"""

#PROGRAM

n=int(input("ENTER THE LENGTH OF THE LIST\n"))
l=[]
print("ENTER VALUES INTO THE LIST")
for i in range(n):
    l.append(int(input()))

m=list(set(l))
for i in range (len(m)):
    s=l.count(m[i])
    print(m[i],"-",s)

    

#TESTED INPUTS AND OBTAINED OUTPUTS:
#INPUT-1:
"""
ENTER THE LENGTH OF THE LIST
19
ENTER VALUES INTO THE LIST
1
2
3
5
8
4
7
9
1
4
12
5
6
5
2
1
0
8
1
0 - 1
1 - 4
2 - 2
3 - 1
4 - 2
5 - 3
6 - 1
7 - 1
8 - 2
9 - 1
12 - 1"""

#INPUT-2:
"""
ENTER THE LENGTH OF THE LIST
6
ENTER VALUES INTO THE LIST
1
2
33
1
2
3
1 - 2
2 - 2
3 - 1
33 - 1
>>> 

"""

