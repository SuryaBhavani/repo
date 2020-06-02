#PROBLEM-4:
'''Develop a program to calculate the total and individual player scores in a cricket match. 
Input would be an array with the index representing the ball number and the value representing the runs scored of that ball.

Assumptions/Tips:
1.	No Extras bowled
2.	Batsman has to be rotated after ever over
3.	Bowler can bowl any number of overs
4.	Assume Batsman 1 is on strike for the first ball.


Below is an example:

Input : [1,2,0,0,4,1,6,2,1,3];

Output:
Total Score: 20
Batsman 1 Score : 4 (1 + 3)
Batsman 2 Score : 16 (2 + 4 + 1 + 6 + 2 + 1)'''


#PROGRAM
n=int(input("Enter the length of list:\n"))
l=[]
print("Enter the values into the list:\n")
for i in range(n):
    l.append(int(input()))
b1=[]
b2=[]
count=1
flag=True
for i in range(len(l)):
    if l[i]%2!=0 and flag == True and count%6!=0:
        b1.append(l[i])
        count+=1
        flag=False
    elif l[i]%2==0 and count%6!=0 and flag == True:
        b1.append(l[i])
        count+=1
        continue
        flag=False
    elif l[i]%2!=0 and flag == False and count%6!=0:
        b2.append(l[i])
        count+=1
        flag=True
  
        
    elif l[i]%2==0 and flag == False and count%6!=0:
        b2.append(l[i])
        count+=1
        continue
        flag=True
    else:
        if count%6==0 and l[i]%2==0:
            if flag==True:
                b1.append(l[i])
                count+=1
            else:
                b2.append(l[i])
                flag=True
                count+=1
        elif count%6==0 and l[i]%2!=0:
            if flag==True:
                b1.append(l[i])
                count+=1
            else:
                b2.append(l[i])
                count+=1
        

print("Total=",sum(l))
print("batsman_1 score= ",sum(b1),"(",'+'.join(map(str, b1)),")")
print("batsman_2 score=",sum(b2),"(",'+'.join(map(str, b2)),")")



#TESTED INPUTS AND OBTAINED OUTPUTS:
#Input:1
"""
Enter the length of list:
10
Enter the values into the list:

1
2
0
0
4
1
6
2
1
3
Total= 20
batsman_1 score=  4 ( 1+3 )
batsman_2 score= 16 ( 2+0+0+4+1+6+2+1 )
>>> """
#Input:2
"""
Enter the length of list:
10
Enter the values into the list:

1
2
0
0
4
2
6
2
1
3
Total= 21
batsman_1 score=  10 ( 1+6+2+1 )
batsman_2 score= 11 ( 2+0+0+4+2+3 )
>>> 
    """
    
