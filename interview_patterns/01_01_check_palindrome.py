# def palindrome_check(str):
#     rev = ''
#     for ch in str:
#         rev = ch + rev
#
#     if str == rev:
#         return True
#     else:
#         return False
#
#
# if palindrome_check("hello"):
#     print("Palindrome")
# else:
#     print("not palindrome")

##################################################

# def palindrome_check(s):
#     rev = ''
#     for ch in s:
#         rev = ch + rev
#     return s == rev
#
#
# if palindrome_check("madam"):
#     print("Palindrome")
# else:
#     print("not palindrome")


####################################################

# def check_pal(str):
#     return str == str[::-1]
#
#
# res = check_pal("hello")
# if res:
#     print("Palindrome")
# else:
#     print("Not palindrome")
##########################################

s = "hello"
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")

