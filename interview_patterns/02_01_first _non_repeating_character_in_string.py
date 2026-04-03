s = "swiss"
seen = {}
for ch in s:
    if ch in seen:
        seen[ch] += 1
    else:
        seen[ch] = 1

print(seen)
for ch in seen:
    if seen[ch] == 1:
        print(ch)
        break
