s = input()
i = int()
s = s[::-1]
for y in range(len(s)):
    i = i + int(s[y]) * (2 ** y)
print(i)
