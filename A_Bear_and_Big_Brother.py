limak, bob = map(int, input().split())
trigger = True
count = 0
while(trigger):
    if limak > bob: 
        print(count)
        break
    else:
        limak*=3 
        bob*=2 
        count+=1 
