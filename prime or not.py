#python script to check whether a given number is prime or not>
def prime():
    n=int(input("enter value:"))
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if count==2:
        print(n,"is prime")
    else:
        print(n,"is not prime")
        
