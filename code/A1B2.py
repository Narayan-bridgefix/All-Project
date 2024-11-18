print(380*20)
s = input("Enter String with number :- ")
a = "1234567890"
# b = ""
final = ""
i = 0
while i < len(s) - 1:
    alph = ""
    while i < len(s) - 1 and (s[i] not in a):
        alph += s[i]
        i += 1
    num = ""
    while i < len(s) and (s[i] in a):
        num += s[i]
        i += 1
    if i == len(s):
        if num:
            final += alph * int(num)
        else:
            final += alph
    else:
        if num:
            final += alph * int(num)
        else:
            final += alph

if s[-1] not in a:
    final += s[-1]
print(final)
# cur = s[0]
# for i in range(1,len(s)):
#     if s[i] in a:
#         b+=s[i]
#     else:
#         if b=="":
#             final+=cur
#             cur=s[i]
#         else:
#             final+=cur*int(b)
#             b=""
#             cur=s[i]
# if b:
#     final+=cur*int(b)
# else:
#     final+=cur
# print(final)
