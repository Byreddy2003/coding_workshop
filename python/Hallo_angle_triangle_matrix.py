print("enter your value :")
row=int(input())
for i in range(1,row+1):
    if i==1 or i==row:
        print('*'* i)
    else:
        print('*'+ ' '*(i-2)+'*')
