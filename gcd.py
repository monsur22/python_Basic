n1=6
n2=3

sum=n1+n2
while(n2!=0):
    temp=n1%n2
    n1=n2
    n2=temp

print("GCD:",n1)

LCD=sum/n1

print(LCD)