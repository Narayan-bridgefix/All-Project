arr=[0,0,0,0,0,0,0,0,0,0]
arr=[1 for i in range(len(arr))]
# print(arr)
for i in range(2,len(arr)+1):
    for j in range(i,len(arr)+1):
        if j%i==0:
            if arr[j-1]==0:
                arr[j-1]=1
            else:
                arr[j-1]=0
print(arr)