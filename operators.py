Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Arithmetic
a=3
b=9
print(a+b)
12
print(a-b)
-6
print(a*b)
27
print(a//b)
0
print(a/b)
0.3333333333333333
print(a**b)
19683
print(a%b)
3
#assignment
a=3
b=4
print(a+=b)
SyntaxError: invalid syntax
a
3
=
a+=b
b
4
a-=b
b
4
a*=b
b
4
a//=b
b
4
b+=a
b
7
b-=a
b
4
b*=a
b
12
b//=a
b
4
b/=a
b
1.3333333333333333
b**=a
b
2.37037037037037
b%=a
b
2.37037037037037
#Comprehension
a=3
b=6
a<b
True
b<a
False
a>b
False
a<b
True
a!=b
True
a==b
False
a<=b
True
b<=a
False
b>=a
True
a>=b
False
a==b
False
#Logical
a=3
b=6
a<b and b>a
True
a<=b and b>==a
SyntaxError: invalid syntax
a<=b and b>=a
True
a!=b and a==b
False
a<b or a>b
True
>>> a<=b or b>=a
True
>>> not True
False
>>> not False
True
>>> #Identify
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> b=3.8
>>> type(b) is float
True
>>> type(b) is not float
False
>>> c="ammu"
>>> type(c) is string
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    type(c) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
>>> c="code"
>>> type(c) is str
True
>>> type(c) is not str
False
>>> d=2+3j
>>> type(d) is complex
True
>>> type(d) is not complex
False
>>> f=True
>>> type(f) is bool
True
>>> type(f) is not bool
False
>>> # Membership
>>> a=2,3,4,5,6,7
>>> 8 in a
False
>>> 3 in a
True
>>> 9 not in a
True
