'''
打印100- 999之间的所有水仙花数
153 = 1**3+5**3+3**3
153就是水仙花数
'''


for i in range(100,1000):
    a = i % 10
    b = i //10 % 10
    c = i // 100
    if a**3 + b**3 + c ** 3 == i:
        print(i)










