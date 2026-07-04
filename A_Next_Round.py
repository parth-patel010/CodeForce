
n1, n2 = map(int, input().split())
nums = list(map(int, input().split()))

target = nums[n2 - 1]
count = 0

for i in range(len(nums)):
    if nums[i] > 0 and nums[i] >= target:
        count += 1

print(count)