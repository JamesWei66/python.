a,b = input().split()
a,b = eval(a,),eval(b)
if(a>b):
    print("Invalid.")
else:
    print("fahr celsius")
    i = a
    while i <= b:
        print("{:d}{:>6.1f}".format(i,5*(i - 32)/9))
        i += 2







#打怪的错误示范！！！应该简约一点
#lower,upper = map(int,input().split())
#c1 = 0
#c2 = 0
#c3 = 0
#if lower < upper:
#   c1 = 5*(lower - 32)/9
#   c3 =lower + 2
#   c2 = 5*(c3 - 32)/9
#   print(f"fahr celsius\n{lower}   {c1}\n{c3}   {'%.1f'%c2}")

#while lower > upper:
#   print("Invalid.")
#   break
