Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",6+3j,True,False]
print(a)
[2, 4.5, 'python', (6+3j), True, False]
type(a)
<class 'list'>
b=9
type(b)
<class 'int'>
c=[3]
type(c)
<class 'list'>
#append
a=["python","c","c++","java"]
a.append("dsa")
a
['python', 'c', 'c++', 'java', 'dsa']
#extend
a=["pra","mas","pos"]
a.extend(["c","c++","java"])
a
['pra', 'mas', 'pos', 'c', 'c++', 'java']
#insert
b=["vja","viz"]
b.insert(1,"hyd")
b
['vja', 'hyd', 'viz']
#index
a=["blue","black","red"]
a.index("red")
2
#copy
a.copy()
['blue', 'black', 'red']
b=a.copy()
b
['blue', 'black', 'red']
b.count("red")
1
#SORT()
a=["apple","banana","grapes","mango"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[6,5,4,3,1]
b.sort()
b
[1, 3, 4, 5, 6]
#reverse
a=["maha","teddy","pranathi","prameela"]
a.reverse()
a
['prameela', 'pranathi', 'teddy', 'maha']
b=[9,8,7,6,5,4,3,2,1]
a.reverse()
b.reverse()
b
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

a=["C","PYT","c++","java"]
a.pop()
'java'
>>> a.pop(2)
'c++'
>>> a.remove("c++")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.remove("c++")
ValueError: list.remove(x): x not in list
>>> a
['C', 'PYT']
>>> a.remove("c")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.remove("c")
ValueError: list.remove(x): x not in list
>>> a.remove("C")
>>> A
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
>>> a
['PYT']
>>> ['PYT']
['PYT']
>>> 
>>> a=["ammu","chitti","maha","teddy"]
>>> len(a)
4
>>> b="prameela"
>>> len(b)
8
>>> b=["prameela"]
>>> len(b)
1
>>> a.clear(a)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a.clear(a)
TypeError: list.clear() takes no arguments (1 given)
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
