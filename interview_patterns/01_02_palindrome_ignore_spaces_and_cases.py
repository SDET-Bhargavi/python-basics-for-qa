# "Madam" → Palindrome
# "nurses run" → Palindrome
# "Hello" → Not palindrome

s = "nurses run"
new =s.lower().replace(" ", "")

for i in range(len(new)//2):
    if new[i] != new[-(i+1)]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")
