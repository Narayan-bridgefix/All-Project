arr = [[1,9],[11,20],[19,30],[11,40]]
i = arr[0][0]
j = arr[0][1]
final = []
for k in range(1,len(arr)):

    if arr[k][0] < j:
        j = arr[k][1]
    elif arr[k][0] > i:
        final.append([i,j])
        i=arr[k][0]
        j=arr[k][1]
final.append([i,j])
print(final)