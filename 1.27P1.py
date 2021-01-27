a,b,c = map(int,input().split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("%d->%d->%d" % (a, b, c))



#运用了if进行比较了，然后替换位置，适合数量少的比较