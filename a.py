#  result = list()
#  score_total = (66, 55, 46, 87, 77, 98, 55, 70, 67, 60, 79, 86)
#  for i in score_total:
#      if i > 60:
#          result.append(i)
#  print(result)
#<++>
#  result_1 = list()
#  result_2 = list()
#  score_total = (66, 55, 46, 87, 77, 98, 55, 70, 67, 60, 79, 86)
#  for i in score_total:
#      if i > 60:
#          result_1.append(i)
#  for i in score_total:
#      if i < 60:
#          result_2.append(i)
#  result_2.sort(reverse=True)
#  result_1.sort(reverse=True)
#  print(result_2)
#  print(result_1)
"""
score = int(input('请输入分数：'))
grade = ''
if score < 60:
    grade = '不及格'
if 60 <= score < 80:
    grade = '及格'
if 80 <= score < 90:
    grade = '良好'
else:
    grade = '优秀'
print('分数是{0},等级是{1}'.format(score, grade))
"""
'''
import random

computer = random.randint(1, 3)
i = int(input("你要出什么？1代表石头，2代表剪刀，3代表布"))
if i == computer:
     print("平局")
elif (computer == 1 and i == 3) or (computer == 2 and i == 1) or (computer == 3 and i == 2):
     print("你赢了")
else:
     print("你输了")
print(computer, "---", i)
'''
'''
d = {"小明":23, "李华": 25, "杰克":22, "威廉":19, "爱丽丝": 19, "托马斯": 37}
for key in list(d.keys()):
    if d[key]<25:
        del d[key]
print (d)
'''

#  a_list = [
#      1,
#      4,
#      6,
#      4,
#      7,
#      12,
#      3,
#      24,
#      6,
#      55,
#      77,
#      43,
#      3,
#      5,
#      77,
#  ]
#  for i in range(len(a_list)):
#      if a_list[i]> 10:
#          print(a_list[i])
#  exit()
#  import random
#  for i in range(100):
#      a = random.randint(1, 9)
#      b = input("请输入1-9一个数")
#      if a == b:
#          print("你猜对了")
#          exit()
#      if str(b) == 'q':
#  exit()
#  a = int(input("请输入一个自然数"))
#
#
#  def is_prime2(x):
#      for i in range(2, int(x ** 0.5) + 1):
#          if x % i == 0:
#              return False
#      return True
#
#
#  print(is_prime2(a))

#  from typing import List
#  from numpy import mean
#
#  sum = [1, 2, 2, 20, 19, 18, 99, 100]
#
#
#  def list_describe(List):
#      if not isinstance(List, list):
#          #判断输入的类型是否是list
#          print("please input a list type")
#          return None
#      return max(List), min(List), mean(List)
#
#
#  print(list_describe(sum))
#  def myfac(a):
#      if a == 1:
#          return 1
#      else:
#          return a * myfac(a - 1)
#      pass
#
#
#  list = []
#  for i in range(1, 21):
#      list.append(myfac(i))
#  print(sum(list))

#  def mysum(n):
#  if n == 1:
#      return 1
#  else:
#      return n + mysum(n - 1)
#
#
# print(mysum(100))

#  a = [1, 2, 5, 65, 7, 78, 8, 100]
#  max1 = a[0]
#  max2 = 0
#  min1 = a[0]
#  min2 = 0
#  for i in range(len(a)):
#      if a[i] > max1:
#          max1 = a[i]
#          max2 = i
#  for i in range(len(a)):
#      if a[i] < min1:
#          min1 = a[i]
#          min2 = i
#  d = a[0]
#  a[0] = a[max2]
#  a[max2] = d
#
#  d = a[7]
#  a[7] = a[min2]
#  a[min2] = d
#  print(a)

#  a = [1, 23, 3, 3, 34, 3, 3, 3, 3]
#  print(a[::-1])

#  a = [1, 23, 3, 3, 34, 3, 3, 3, 3]
#  for i in range(len(a)):
#      if a[i] == a[len(a) // 2]:
#          exit(a)
#      else:
#          d = a[i]
#          a[i] = a[len(a) - 1 - i]
#  a[len(a) - 1 - i] = d

#  a = [1, 2, 34, 5, 6, 7, 87, 8, 9, 9]
#  m = int(input())
#  b =a[:11-m]
#  c = a[-m::]
#  a =   c+b
#  print(a)
#  import random
#
#  x = [random.randint(0, 100) for i in range(20)]
#  print(x)
#  y = x[::2]
#  y.sort(reverse=True)
#  x[::2] = y
#  print(x)

#  def mab(num):
#      i = 2
#      list1 = []
#      while True:
#          if num % i == 0:
#              num = num // i
#              list1.append(i)
#              i = 1
#          if num // 2 == i:
#              list1.append(num)
#              break
#          i += 1
#      return list1
#
#
#  num = 12
#  print(mab(num))
#  def selection_sort(list):
#      length = len(list)
#      for i in range(length - 1, 0, -1):
#          for j in range(i):
#              if list[j] > list[i]:
#                  list[j], list[i] = list[i], list[j]
#      return list
#
#
#  list1 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 3, 2]
#  print(selection_sort(list1))

#  def bubble_sort(list):
#      count = len(list)
#      for i in range(count):
#          for j in range(i + 1, count):
#              if list[i] > list[j]:
#                  list[i], list[j] = list[j], list[i]
#      return list
#
#
#  list1 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 3, 2]
#  print(bubble_sort(list1))
'''
Name = 'lihang'
age = 18
grade = 90
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
list = ['才叫教程', 'www.runoob.com']
print("网站名:{0[0]},地址{0[1]}".format(list))
'''
'''
#  format函数斗鱼基本字符串字典列表的引用
list = [1, 2, 3, 4, 5]
a, *b, c = list
print(a, b, c) #a和b返回的是整行赋值b是一个列表赋值
dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
a, b, *c = dictionary
print(a, b, c)#字典的解包只能解包建不能解包值
'''
students = {'001': ('Alice', 19), '002': ('Bob', 21), '003': ('Mark', 31)}

#  def print_boy(persons):
#  if isinstance(persons, dict):
#      values = persons.values()
#      print(values)
#      for name, age in values:
#  print('{}的年龄是:{}'.format(name, age))
'''
def func(*args, **kwargs):
    print(*args)
    if isinstance(args, list):
        for i in args:
            print(args)
    else:
        print('args is not a list!')

    for v, k in kwargs.items():
        print('这个字典的键为{},值为{}'.format(k, v))


list1 = [1, 2, 3, 4, 5]
dict1 = {'luis': 100, 'rose': 150}
func(*list1, **dict1)
'''
'''
def main(**kwargs):
    key_list = []
    value_list = []
    for k, v in kwargs.items():
        key_list.append(k)
        value_list.append(v)
    return key_list, value_list


dict_grade = {'zhouhao': 100, 'zhangyuchao': 0, 'Mark': 50}
# result = main(**dict_grade)
# print(result)  # 返回类型  --> 元组
key, value = main(**dict_grade)
print(key, value, sep='---') #sep两个元组之间用---连接
'''
'''
def decorate(func):
    a=10# 传递的参数一定要为函数
    def wrapper():
        print('operation one')
        func() # 调用函数
        print('operation two')
        print(a)
    return wrapper
# 使用装饰器
@decorate
def testfunc():
    print('......')
def outer(args): # 第一层负责接收装饰器的参数的
    def decorate(func): # 第二层是负责接收函数的
        def wrapper(*args,**kwargs): # 第三层负责接收函数的参数的
            func(*args,**kwargs)
            pass
        return wrapper # 返回第三层函数地址
    return decorate # 返回第二层函数地址

@outer(10)
def test(time):
    print('-----')
import time
import functools
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper

import functools
def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ... # 检查输入是否合法
'''
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()
print(now.__name__)
'''
'''
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()
print(now.__name__)
#上述函数的名字会改变因为返回的是wrapper
#所以完整的装饰器如下functools.wraps能够解决这个name变量改变的问题
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2020-2-2')
now()
print(now.__name__)

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
    '''
'''
#返回函数的解析
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f =lazy_sum(1,2,3,4,4,)
print(f)
print(f())
'''
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
'''
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())
'''
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
#发现结果都是9因为外层函数并非立即执行等三个函数都返回时他们所引用的i都变成了3
#局部变量在外层时直接x并没有初始化所以我们在内层函数想要引用外层局部变量时要在内层函数加nonlocal x
def inc():
    x = 0
    def fn():
        # nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # 1
print(f()) # 2
'''
'''
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#lambda表示匿名函数id
f = lambda x: x * x
print(f)
print(f(5))

def build(x, y):
    return lambda: x * x + y * y
if __name__=='__main__':
    print(build(2,1))
'''
'''
int('12345', base=8) #可以讲12345转换成8进制的值
def int2(x, base=2):
    return int(x, base)
#创建了转换进制的函数int2
'''
#类和实例
#__init__的方法是Student类里的私有方法这种把方法放在类里的方法也叫封装
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
'''
"""
#  类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#
#  方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#
#  通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#
#  和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
"""

#  list_1=list(input().split())
#  list_1=[int(i) for i in list_1]
#  avg=sum(list_1)/len(list_1)
#  list_2=[i for i in list_1 if i>avg]
#  print(list_2)
'''
list_1=list(input().split( ))
list_1=[int(i) for i in list_1]
avg=sum(list_1)/len(list_1)
list_2=[i for i in list_1 if i>avg]
for i in list_2:
    print(i,end=' ')
    '''

#  a = 1
#  while a:
#
#      try:
#          a = int(input('请输入一个数字'))
#          b = int(input('请输入另一个数字'))
#      except ValueError:
#          a = 1
#          print('类型错误请输入两个数字')
#
#      else:
#          a = 0
#          c = a + b
#  print(c)
#  def read_file(filename):
#      try:
#          with open(filename) as file_seion:
#              contents = file_seion.read()
#      except FileNotFoundError as e:
#          pass
#      else:
#          print(contents.strip())
#      pass
#
#
#  file = ['cats.txt', 'dogs.txt']
#  for i in file:
#      read_file(i)
#      pass

#  try:
#      with open('./Pride and Prejudice.txt') as s:
#          file_dict = s.read()
#          c = str(input())
#      b = file_dict.count(c)
#      print(b)
#  except FileNotFoundError as e:
#      print("文件不存在")
#  except ValueError:
#  print("类型输入错误")
#  def sum(dict):
#      for item in dict:
#          print('股票名字:', item['name'], '股票的总价:', item['shares'] * item['price'])
#
#
#  def over_price(dict):
#      return dict['price'] > 100
#
#
#  portfolio = [{
#      'name': 'IBM',
#      'shares': 100,
#      'price': 91.1
#  }, {
#      'name': 'AAPL',
#      'shares': 50,
#      'price': 543.22
#  }, {
#      'name': 'FB',
#      'shares': 200,
#      'price': 21.09
#  }, {
#      'name': 'HPQ',
#      'shares': 35,
#      'price': 31.75
#  }, {
#      'name': 'YHOO',
#      'shares': 45,
#      'price': 16.35
#  }, {
#      'name': 'ACME',
#      'shares': 75,
#      'price': 115.65
#  }]
#  sum(portfolio)
#  print('单价大于100的股票有:', list(filter(over_price, portfolio)))
