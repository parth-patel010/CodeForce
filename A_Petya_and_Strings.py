words = []
count = 0
for i in range(2):
    words.append(input().split())

for i in range(len(words[0])):
    if words[0][i].lower() == words[1][i].lower():
        print(0)
        
    elif words[0][i].lower() > words[1][i].lower():
        print(1)
        
    else:
        print(-1)

