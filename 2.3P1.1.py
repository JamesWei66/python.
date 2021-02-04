sg = list(map(int, input().split(" ")))
for item in sg:
    if item > sum(sg)/len(sg):
        print('{:d}'.format(item), end=" ")