# "A man, a plan, a canal: Panama" - Palindrome

# s = "A man, a plan, a canal: Panama"
# cleaned = ""
#
# for ch in s:
#     if ch.isalnum():
#         cleaned += ch.lower()
#
# if cleaned != cleaned[::-1]:
#     print("Not Palindrome")
# else:
#     print("Palindrome")


##################################################

def check_palindrome_ignore_cases_spaces_special_characters(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned = cleaned + ch.lower()
    return cleaned == cleaned[::-1]


if check_palindrome_ignore_cases_spaces_special_characters("A man, a plan, a: canal Panama"):
    print("Palindrome")
else:
    print("not palindrome")