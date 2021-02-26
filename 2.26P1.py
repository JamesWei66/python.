a = input()
b = input()
if b.find(a) != -1:
    b = b[::-1]
    print('index = {:d}'.format(len(b) -  b.find(a) - 1))
else:
    print('Not Found')







"""
我自己写的 =_="    计算正确，但是格式错误和未能返回正确结果
m1 = input()
m2 = input()
length = len(m2)
index = 0
cnt = 0
for i in range(length):
    if m1 == m2[i]:
        print("index = ", i + 1)
        cnt = 1
        break
if cnt == 0:
    print("Not Found")
"""




