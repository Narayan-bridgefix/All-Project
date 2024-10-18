import random
while True:
    flag=False
    l=0
    h=51
    x = random.randrange(1, 50)
    print(x,"x----")
    for i in range(5):
        num = int(input("Enter the number between 1 to 50 :- "))
        if x==num:
            flag=True
            break
        elif x>num:
            # l=1
            h=num+1
            print("Number is Greter")
        elif x<num:
            l=num-1
            # h=50
            print("Number is lower")
    if flag==True:
        print("Win the game! the number is:- ",x)
    else:
        print("Failed")
    n = int(input("Enter 1 if you dont want to play game Or Enter 2 to continue :- "))
    if n==1:
        break
    else:
        continue
    