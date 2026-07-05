matrix = []
count = 0
for i in range(5):
    matrix.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            for k in range(5):
                if j == 2:
                    break
                if j >= 2:
                    j-=1
                    count+=1
                else:
                    j+=1
                    count+=1

            for x in range(5):
                if i == 2:
                    print(count)
                    break
                if i >=2:
                    i-=1
                    count+=1
                else:
                    i+=1
                    count+=1