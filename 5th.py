n=input("enter String ")
#read input from user
n=n.replace(" ","")
#replace space with empty space 
u=0
l=0
#using loop to traverse input
for i in n:
    #using isupper() function to find upper case or not ,else lower case
    if(i.isupper()):
        u=u+1
        #increment uppercase count by 1
    else:
        l=l+1
        #increment lower case count by 1
print("No. of Upper-case characters:",u)
print("No. of Lower-case Characters:",l)