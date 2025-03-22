#coding class on 21-03-2025

"""

#print * in a squre martix
print("enter your value :")
rows=int(input())
for i in range(1,rows+1):
    print('*'* rows)

    

#To print hallo square matrix
print("enter your value :")
row=int(input())
for i in range (1,row +1):
    if i==1 or i==row:
        print('* ' * row)
    else:
        print('* '+'  '*(row-2)+'*')


#To print hallo right angle triangle matrix
print("enter your value :")
row=int(input())
for i in range(1,row+1):
    if i==1 or i==row:
        print('*'* i)
    else:
        print('*'+ ' '*(i-2)+'*')


#To print upper right angle triangle matrix
print("enter your value :")
row=int(input())
for i in range(1,row+1):
    print('*'*(row-i))

"""
#To print upper right angle triangle matrix
print("enter your value :")
row=int(input())
for i in range(1,row+1):
    print(' '*(row-i)+'*'*(2*i-1))

testing