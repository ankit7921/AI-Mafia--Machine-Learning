l=[8,3,4,1,5,9,6,7,2]
l1=[]
l3=[]
for i in range(len(l)):
    l1.append(int(input()))
for i in range(0,len(l1)):
    if l[i]-l1[i]>0:
        l3.append(l[i]-l1[i])
    else:
        l3.append(l1[i]-l[i])

print(sum(l3))
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
c=0
l=[]
def fun(num):
    c=0
    for i in range(1,num):
        if num%i==0:
            c=c+i
    if c==num:
        return 2
    else:
        return 3


for i in range(n):
    t=fun(arr[i])
    if t==2:
        print("YES")
    else:
        print("NO")

