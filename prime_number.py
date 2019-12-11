# n=80
# if n%2!=0 or n==1:
#     print("Prime")
# else:
#     print("Not Prime")



# def prime(n):
#     for i in range(2,n):
#         if n%i ==0:
#             print("Not Prime")
#             break
#     else:
#         print(" Prime")
#     return ""
# print(prime(7))





def prime(n):
    for i in range(0, n + 1): 
         if i > 1 and i!=2: 
            for j in range(2, i): 
                if (i % j) == 0: 
                    break
            else: 
                print(i) 
    return ""
print(prime(10))

