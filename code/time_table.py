day = ["mon","tues","wednus","thurs","fri","suter"]
dict = {}
maxx = {}
for i in day:
    max_l = 9
    for j in range(1,5):
        inp = input("Enter the subject for "+i+"day lecture "+str(j)+":-")
        max_l=max(max_l,len(inp))
        inp_format=i+"_"+str(j)
        dict[inp_format]=inp
    maxx[i]=max_l
print(maxx)
a=0
for i in maxx:
    a+=maxx[i]
print(a)
# dict ={'mon_1': 'hind', 'mon_2': 'english', 'mon_3': 'maths', 'mon_4': 'science', 'tues_1': 'hindi', 'tues_2': 'english', 'tues_3': 'maths', 'tues_4': 'science', 'wednus_1': 'hindi', 'wednus_2': 'science', 'wednus_3': 'english', 'wednus_4': 'maths', 'thurs_1': 'hindi', 'thurs_2': 'english', 'thurs_3': 'maths', 'thurs_4': 'science', 'fri_1': 'hindi', 'fri_2': 'english', 'fri_3': 'maths', 'fri_4': 'science', 'suter_1': 'hindi', 'suter_2': 'maths', 'suter_3': 'science', 'suter_4': 'sans'}
print("-"*(a+33))
print("|","   Time "," "*2,"|","Monday".center(maxx['mon']),"|","Tuesday".center(maxx['tues']),"|","Wednusday".center(maxx['wednus']),"|","Thursday".center(maxx['thurs']),"|","Friday".center(maxx['fri']),"|","Saturday".center(maxx['suter']),"|")
print("-"*(a+33))
print("|","10:00-11:00","|",dict['mon_1'].center(maxx['mon']),"|",
      dict['tues_1'].center(maxx['tues']),"|",
      dict['wednus_1'].center(maxx['wednus']),"|",
      dict['thurs_1'].center(maxx['thurs']),"|",
      dict['fri_1'].center(maxx['fri']),"|",
      dict['suter_1'].center(maxx['suter']),"|"
      )

print("-"*(a+33))
print("|","10:00-11:00","|",dict['mon_2'].center(maxx['mon']),"|",
      dict['tues_2'].center(maxx['tues']),"|",
      dict['wednus_2'].center(maxx['wednus']),"|",
      dict['thurs_2'].center(maxx['thurs']),"|",
      dict['fri_2'].center(maxx['fri']),"|",
      dict['suter_2'].center(maxx['suter']),"|"
      )
print("-"*(a+33))
print("|","10:00-11:00","|",dict['mon_3'].center(maxx['mon']),"|",
      dict['tues_3'].center(maxx['tues']),"|",
      dict['wednus_3'].center(maxx['wednus']),"|",
      dict['thurs_3'].center(maxx['thurs']),"|",
      dict['fri_3'].center(maxx['fri']),"|",
      dict['suter_3'].center(maxx['suter']),"|"
      )
print("-"*(a+33))
print("|","10:00-11:00","|",dict['mon_4'].center(maxx['mon']),"|",
      dict['tues_4'].center(maxx['tues']),"|",
      dict['wednus_4'].center(maxx['wednus']),"|",
      dict['thurs_4'].center(maxx['thurs']),"|",
      dict['fri_4'].center(maxx['fri']),"|",
      dict['suter_4'].center(maxx['suter']),"|"
      )
print("-"*(a+33))