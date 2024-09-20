# b = [ ".", ".", "b", ".", "b", ".","b", ".", "b", ".",'b','b']
# b=['b','.','b','.','b','.','b','.','b','.','.','.','b','.','b','.','b']
# b=['.','.','.','b','b','b','b']
# b = ["b", ".", ".", "b", ".", "b", "b"]
# b = ["b", ".", ".",".",".", "b", ".", "b","b","b",'b']
# b=["b",'.','.','.','.','b','.','b','b','b','b']\
b=["b",".",".",".","b","b","."]


arr1 = [i for i in range(len(b)) if b[i] == "b"]
# for i in range(len(b)):
#     if b[i] == "b":
#         arr1.append(i)
# print(arr1)
arr2 = [i for i in range(0, len(b), 2) if i not in arr1]
# for i in range(0, len(b), 2):
#     if i not in arr1:
#         arr2.append(i)
k = 0
arr3 = arr1.copy()
while k < len(arr3):
    if arr3[k] % 2 == 0:
        arr3.pop(k)
    else:
        k += 1
print(arr2, arr3)


if len(arr2) < len(arr3):
    print(-1)
else:
    c = 0
    i = 1
    flag = True
    while i < len(arr1):
        if (arr1[i] - arr1[i - 1]) == 1:
            if arr2:
                c+=2
                var=arr2.pop(0)
                if arr1[i]%2==1:
                    arr1.remove(arr1[i])
                else:
                    arr1.remove(arr1[i-1])
                # if i+1<len(arr1) and arr1[i-1]==arr1[i]-1 and arr1[i+1]==arr1[i]+1 and arr1[i]%2==1:
                #     arr1.remove(arr1[i])
                # elif i+1<len(arr1) and arr1[i-1]==arr1[i]-1 and arr1[i+1]==arr1[i]+1 and i+1==len(arr1)-1:
                #     arr1.remove(arr1[i])
                # elif arr1[i-1]%2==1:
                #     arr1.remove(arr1[i-1])
                # else:
                #     arr1.remove(arr1[i])
                for n in range(len(arr1)):
                    if arr1[n]>var:
                        arr1.insert(n,var)
                        i=n
                        break
            else:
                i += 1
                flag = False
                break
        else:
            i+=1
    if flag:
        print("swap", c)
    else:
        print(-1)