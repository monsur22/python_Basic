# n=153
# def armstrong(n):
#     i=int(n)
#     sum=0
#     while(n>0):
#         sum=sum+(n%10)*(n%10)*(n%10)
#         n=n//10
#     if i==sum:
#         print("Yes")
#     else:
#         print("Not")

#     return ""
# print(armstrong(n))
num=153
def arm(num):
    tem=num
    sum=0
    while num>0:
        sum=sum+(num%10)*(num%10)*(num%10)
        num=num//10
    if tem==sum:
        print("Y")
    else:
        print("N")

    return ""
print(arm(num))