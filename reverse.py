# def rev(num):
#     num=str(num)
#     arr=list(num)
#     b="".join(arr)
#     # return arr
#     return b
# print(rev(123))

# num=[1,2,3]    
# def rev2(num):
#     l=len(num)
#     arr=[]
#     for i in range(l,0,-1):
#         arr.append(i)
#         print(i)
#     return arr
# print(rev2(num))

# num=123
# def rev3(num):
#     a=str(num)
#     arr=list(a)
#     l=len(arr)
#     print(arr)
#     newarr=[]
#     for i in range(l,0,-1):

#         newarr.append(i)
#         print(i)
    
#     return newarr
# print(rev3(num))


# num=['1', '2', '3']
# def rev4(num):

#     b="".join(num)
#     return b
# print(rev4(num))


n="monsur"
def rev(n):
    a=str(n)
    b=list(a)
    l=len(b)
    newarr=[]
    print(a)
    for i in range(l):
        newarr.append(a[l-i-1])
        print(i)

    return newarr
print(rev(n))