A,B =map(int,input().split())
sum = 0
for i in range(A,B+1):
    print("%5d"%i,end="" if (i-A+1)%5 and i!=B else"\n")
    sum += i
print("Sum = {}".format(sum))
