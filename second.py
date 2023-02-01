l=list(map(int,input("enter elements").split(" ")))
#Read input from user , convert into intergers
#using for loop starts from 0 to len(l)
for i in range(0,len(l)):
    #if index not divided by 2 ,which means odd number
    if(i%2!=0):
        print(i,"th index element :",l[i])