Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a=(2,4.5,"ammu",3+5j,True,False)
>>> print(a)
(2, 4.5, 'ammu', (3+5j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.count(True)
1
>>> a.inex(False)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.inex(False)
AttributeError: 'tuple' object has no attribute 'inex'. Did you mean: 'index'?
>>> a.index(False)
5
