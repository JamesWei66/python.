sg = list(map(int, input().split()))
m = len(sg)
n = sum(sg)
avg = int(n/m)


for i in range(0, m):
    if sg[i] > avg:
        print('{:d}'.format(sg[i]), end=" ")









