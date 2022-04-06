# class Node:
#     def __init__(self, value ,next = None):
#         self.value = value
#         self.next = None
#
# class SLL:
#     def __init__(self):
#         self.head = None
#
#     def Addvalue(self,v, next = None):
#         v = Node(v)
#         self.head = v

#
#
#
# mainhead = SLL().head = Node(5)
# node2 = SLL().value = Node(12)
# node3 = SLL().value= Node(6)
# node4 = SLL.Addvalue(node3,23)
#
#
# mainhead.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = None
#
# while mainhead:
#
#     print(mainhead.value)
#     mainhead = mainhead.next
#     if mainhead is None:
#         print("None")
#         break
#
# def sumN ():
#     print("Enter a number")
#     n = int(input())
#     sum = 0
#     i = 1
#     while i < n:
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i
#             i += 1
#         else:
#             i +=1
#     print (sum)
# sumN()
#
# def SumPro():
#     s = "Sum"
#     p = "Prudect"
#     print ("enter a number")
#     n = int(input())
#     print("Write 'Sum' for sum ... prudect")
#     string = str(input())
#     if string == "Sum":
#         i = 1
#         sum = 0
#         while i <= n:
#             sum += i
#             i += 1
#         print(sum)
#     else:
#         j = 1
#         prod = 1
#         while j <= n:
#             prod = prod * j
#             j += 1
#         print (prod)
#
# SumPro()
#
#
#
# def MT():
#     print("enter a number")
#     n = int(input())
#     table = 0
#     for i in range (1,13):
#         table = n * i
#         print ("%d x %d = "%(n,i),table)
#
# MT()
#
# def sumofa():
#     k = 0
#
#     for i in range (1,1000001):
#         k = ((-1)**(i+1))/((2*i)-1)
#     k = 4 * k
#     print (k)
# sumofa()
#
# import random as r
# def  retrunL():
#     lst = []
#     for i in range (50):
#         lst.append(r.randint(1,100))
#     print (lst)
#     for j in range(len(lst)-1):
#         if lst[0]<lst[j]:
#             lst[0]=lst[j]
#     print ("largest number is %d in the list"%lst[0])
#
# retrunL()
#
#
# import random as r
# def revlst():
#     lst = []
#     for k in range (50):
#         lst.append(r.randint(1,200))
#     print (lst)
#     i=0
#     for i in range (len(lst)):
#         if i == 1:
#             break
#         for k in lst[::-1]:
#             lst[i] = k
#             i +=1
#     print (lst)
#
# revlst()
#
# import random as r
#
# def Inlest():
#     lst = []
#     for k in range(5):
#         lst.append(r.randint(1,10))
#     a = int(input("Enter a number from 1 to 10\n"))
#
#     if a in lst:
#         print ("yes %d is in the list"%a)
#     else:
#         print ("try agian :(")
#     print(lst)
#
# Inlest()
#
# import random as r
# import time
# def oodd():
#     lst = []
#     lst2 =[]
#     time1 = time.process_time()
#     for k in range(10):
#         lst.append(r.randint(50,100))
#     for i in lst:
#         if i%2 == 0:
#             pass
#         else:
#             lst2.append(i)
#     print (lst2)
#     print (lst)
#     time2 = time.process_time()
#     tt = time2 - time1
#     print ("this programe took %d sec to execute" %tt)
# oodd()
#
# import random as r
# def sum():
#     lst=[]
#     for k in range(15):
#         lst.append(r.randint(1,10))
#     sum = 0
#     for i in range(len(lst)):
#         sum += lst[i]
#     print (sum)
#     print (lst)
# sum()
#
#
#
import random as r
# def sum(): #while loop
#     lst=[1,2,3,4,5]
#     sum = 0
#     i = 0
#     while i < len(lst):
#         sum += lst[i]
#         i += 1
#     print (sum)
# sum()
#
#
# def sum(lst, n):
#     if len(lst)==1:
#         return lst[0]
#     else:
#         return lst[0]+sum(lst[1:],n)
# lst=[]
# lst = [1, 2, 3, 4, 5]
#
# n = len(lst)
# ans = sum(lst,n)
# print(ans)

# import random as r
# import time
# def squar():
#     lst2 = []
#     lst = []
#     t1 = time.process_time()
#     for j in range (10000):
#         lst.append(r.randint(1,500))
#     for i in range (len(lst)):
#         for k in range (len(lst)-1):
#             if lst[i] == lst[k + 1]:
#                 pro = lst[i] * lst[k + 1]
#                 if pro in lst2:
#                     continue
#                 else:
#                     lst2.append(pro)
#         if len(lst2) == 100:
#             break
#     t2 = time.process_time()
#     t3 = round (t2 - t1,9)
#     print (lst2)
#     print (lst)
#     print("time is %f sec" %t3)
# squar()


import random as r
import math
import matplotlib.pyplot as plt


def pi():
    sum_points = 0
    circal_points = 0
    x_plt = []
    y_plt = []
    for i in range(10000):
        x = r.uniform(0, 1)
        y = r.uniform(0, 1)
        # print (x,y)
        x_plt.append(float(x))
        y_plt.append(float(y))
        cr = x ** 2 + y ** 2
        circal = math.sqrt(cr)

        if circal <= 1:
            circal_points += 1
        sum_points += 1
        pi = 4 * (circal_points) / sum_points
    plt.scatter(x_plt, y_plt)
    plt.show()
    print(pi)


pi()