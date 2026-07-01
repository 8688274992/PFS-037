Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #SETS
>>> a={4,3.4,"ammu",4+5j,True,False}
>>> print(a)
{False, True, 3.4, 4, (4+5j), 'ammu'}
>>> type(a)
<class 'set'>
>>> a={1,2,3,4,5,6}
>>> b={4,5,3,2}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> #superset
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #union
>>> a={1,2,3,4,5,6}
>>> 
>>> b={1,2,3,4}
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> c=[2,2,3,4,5,5,6,7,8,6,9]
>>> print(c)
[2, 2, 3, 4, 5, 5, 6, 7, 8, 6, 9]
>>> c=[2,2,3,4,5,5,6,7,8,6,9}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> c={2,2,3,4,5,5,6,7,8,6,9}
>>> print(c)
{2, 3, 4, 5, 6, 7, 8, 9}
>>> #intersection
>>> a={1,2,3,4,5,5,6,7}
>>> b={3,9,7,5,4}
>>> a.intersection(b)
{3, 4, 5, 7}
>>> #update
>>> a={1,2,3,4,5,6,7}
>>> b={9,8,7,5,4}
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.update(b)
>>> a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> c={1,2,3,4,5,6,7,8}
s={9,7,5,3,2}
c
{1, 2, 3, 4, 5, 6, 7, 8}
c.update(s)
c
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s.update(c)
s
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#difference
x={11,23,2,3,4,7}
c={1,11,3,7,8}
x.difference(c)
{2, 4, 23}
c.difference(x)
{8, 1}
#symmetric difference
a={3,4,25,6,8,7}
b={6,0,2,1,4}
a.symmetric_difference(b)
{0, 1, 2, 3, 7, 8, 25}
#intersection_update
a.intersection_update(b)
a
{4, 6}
b.intersection_update(a)
b
{4, 6}
#difference_update
a.difference_update(b)
b
{4, 6}
c={2,3,4,5,6,7,8}
v={8,6,4,1}
a.difference_update(v)
v
{8, 1, 4, 6}
c
{2, 3, 4, 5, 6, 7, 8}
c.difference_update(v)
c
{2, 3, 5, 7}
v.difference_update(c)
v
{8, 1, 4, 6}
#ssymmetric_difference_update
f={11,12,13,14,15,16,17}
g={12,15,6,17,19}
f.symmetric_difference_update(g)
f
{6, 11, 13, 14, 16, 19}
g.symmetric_difference_update(f)
g
{11, 12, 13, 14, 15, 16, 17}
#pop
z={2,3,4,6,5,8,6}
z.pop()
2
z.pop(3)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    z.pop(3)
TypeError: set.pop() takes no arguments (1 given)
z.remove(3)
z
{4, 5, 6, 8}
#discard
t={1,2,3,4,5}
t.discard(4)
t
{1, 2, 3, 5}
#copy
t.copy()
{1, 2, 3, 5}
#clear
t.clear()
t
set()
#add
t={2}
t
{2}
#LENGTH
len(t)
1

t.count(2)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    t.count(2)
AttributeError: 'set' object has no attribute 'count'
t.index(2)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    t.index(2)
AttributeError: 'set' object has no attribute 'index'
#disjoint
q={1,2,3,4}
w={5,6,7,8}
q.isdisjoint(w)
True
w.isdisjoint(q)
True
