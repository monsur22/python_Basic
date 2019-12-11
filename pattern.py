# p="*"
# def pattern(p):
#     for i in range(5):
#         for j in range(i):
#             print(p,end="")
#         print("")
    
#     return ""



# print(pattern(p))

def p(n):
    for i in range(n):
        for j in range(i):
            print("*",end="")
        print()

    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()
    return ""
print(p(5))