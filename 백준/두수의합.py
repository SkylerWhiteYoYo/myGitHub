n = int(input())
arr = list(map(int,input().split()))
x = int(input())
count = 0
for i in arr:
    if (x-i) in arr:
        count += 1
print(count/2)