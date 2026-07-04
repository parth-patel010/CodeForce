n = int(input())
i = 1;
value = 0
for i in range(n):
    str = input();
    if "x" in str.lower():
        if "+" in str:
            value = value + 1
        elif "-" in str:
            value = value - 1
print(value)