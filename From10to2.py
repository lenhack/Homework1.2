a = int(input())
s = ""
while a >= 1:
    if a % 2 == 0:
        s = s + "0"
    else:
        s = s + "1"
    a = a // 2
s = s[::-1]
print(s)