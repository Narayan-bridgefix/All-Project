# b = [ ".", ".", "b", ".", "b", ".","b", ".", "b", ".",'b'] #res=0
# b=['b','.','b','.','b','.','b','.','b','.','.','.','b','.','b','.','b'] #res=2
# s=['.','.','.','b','.','b','b','.'] #res=2
# b=['b','.','.','b','.','b','b'] #res= 4
#b=['b','b','.','.','.','b'] #res= 2
# b=['b','b','.'] #res= 2
# b=['.','.','.','.','b','.','b','b','.','.','b','b','.'] #res=4
# s=['.','.','b','b','.','.','b','b','.']  #res 4
# s=['b','.','.','.','.','.','b','.','b','.','b','b'] #res=8
#s=bbbb... #res=4
# s=.b.b.b.... #res=4
while True:
    s=input("Enter string ")
    s=list(s)
    if s.count('b')+s.count('.')!=len(s):
        print("Enter only . and b")
    elif len(s)==1 and s[0]=='b':
        print(0)
    elif s.count('b')==0 or s.count('b')-1>s.count('.'):
        print(-1)
    else:
        i=len(s)-1
        j=i-1
        c=0
        while i>=0 and j >=0:
            if (len(s)-1-i)%2==0 and s[i]=='b':
                i-=2
            elif (len(s)-1-j)%2==1 and s[j]=='.':
                j-=2
            else:
                s[i],s[j]=s[j],s[i]
                i-=2
                j-=2
                c+=2
        cnt=s.count('b')
        newarr=list(".b"*cnt)
        newarr.remove('.')
        s=s[::-1]
        for i in range(len(newarr)):
            if s[i]!=newarr[i]:
                c+=2
        print('swap',c)


