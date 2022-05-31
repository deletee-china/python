"""/******************************
 *File name: 1.py
 *Author: lihang
 *Created Time: 五  3/11 15:12:13 2022
 *TODO:"""
'''a=int(input())
b=int(a/2)
for i in range(b+1):
    s1='/'*i
    s2='*'*i
print('{:>10}{:<10}'.format(s1,s2))
'''
'''x = int(input('请输入一个大于2的自然数：'))
P = []
f = []
for i in range(x + 1):
    if i > 2 and i % 2 == 0:
        f.append(1)
    else:
        f.append(0)
i = 3
while i * i <= x:
    if f[i] == 0:
        j = i * i
        while j <= x:
            f[j] = 1
            j += i + i
    i += 2

P.append(2)
for x in range(3, x + 1, 2):
    if f[x] == 0:
        P.append(x)
print(P)'''
'''def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
        else:
            return 1
n=int(input("请输入一个自然数"))
result=set()
result.add(2)
for i in range(2,n):
    if prime(i)==1:
        result.add(i)
print(result)
'''
'''
list_a=input("please enter fist line")
list_a=list(list_a)
list_b=input("please enter second line")
list_b=list(list_b)
dict_ab=dict()
dict_ab=dict(zip(list_a,list_b))
print(dict_ab)
''' '''
from random import random
times=int(input("你投飞镖的次数"))
aa=0
for i in range(times):
    a=random()
    b=random()
    if a*a+b*b<=1:
        aa+=1
print(4*aa/times)
'''
