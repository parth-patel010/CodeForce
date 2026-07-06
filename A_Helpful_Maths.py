words = list(input())
n = len(words)
for _ in range(n):
    for i in range(0, n-2, 2):
        if words[i] > words[i+2]:
            words[i], words[i+2] = words[i+2], words[i]

print("".join(words))