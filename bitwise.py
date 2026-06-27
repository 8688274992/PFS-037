Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Bitwise
a=2
b=4
a&b
0
c=7
n=4
c&n
4
a=4
b=3
a|b
7
s=7
b=8
s|b
15
a=5
-(a+1)
-6
~a
-6
a=-8
~a
7
a=2
b=3
a^b
1
c=4
n=8
c^n
12
a=4
a<<2
16
a=3
a<<4
48
a=4
a>>6
0
c=18
c>>3
2
c=16
c>>3
2
s=22
s>>4
1
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[5]+a[6]
'in'
a[1]+a[4]+a[7]
'   '
a[2]+a[3]
'am'
a="i am learning python course"
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'ython '
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[6]+a[7]+a[8]+a[9]+[10]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a[6]+a[7]+a[8]+a[9]+[10]
TypeError: can only concatenate str (not "list") to str
a[6]+a[7]+a[8]+a[9]+a[10]
'earni'
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> a[21]+a[22]+a[23]+a[24]+a[25]+a[26]
'course'
>>> b="time is very precious"
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
' python '
>>> b13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
SyntaxError: unmatched ']'
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
>>> b[8]+b[9]+b[10]+b[11]
'very'
>>> b[0]+b[1]+b[2]+b[3]
'time'
>>> a="simple is better than complex"
>>> a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'omplex'
>>> a[-23]+a[-24]+a[-25]+a[-26]+a[-27]+a[-28]
' elpmi'
>>> a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
>>> a[19]+a[18]+a[17]
'aht'
=
>>> a[-18]+a[-17]+a[-16]+a[15]+a[14]+a[13]
'ettret'
>>> a+[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a+[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
TypeError: can only concatenate str (not "list") to str
>>> a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
>>> a="i love python"
>>> a[-10]
'o'
>>> a[-11]+a[-10]+a[-9]+a[-8]
'love'
>>> a[-6]
'p'
>>> a[-6]+a[-5]+a[-4]+a[-2]+a[-1]+a[-0]
'pytoni'
>>> a[-6]+a[-5]+a[-4]+a[-2]+a[-1]
'pyton'
