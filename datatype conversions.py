Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# datatype conversions
#int
int(2)
2
int(6.7)
6
int("ammu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("ammu")
ValueError: invalid literal for int() with base 10: 'ammu'
int(3+7k)
SyntaxError: invalid decimal literal
int(True)
1
int(False)
0
#float
float(3)
3.0
float(8.7)
8.7
float("ammu")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("ammu")
ValueError: could not convert string to float: 'ammu'
float(3+9l)
SyntaxError: invalid decimal literal
float(True)
1.0
float(False)
0.0
>>> #string
>>> str(4)
'4'
>>> str(3.8)
'3.8'
>>> str("ammu")
'ammu'
>>> str(3+8g)
SyntaxError: invalid decimal literal
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(4)
(4+0j)
>>> complex(3.7)
(3.7+0j)
>>> complex("ammu")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    complex("ammu")
ValueError: complex() arg is a malformed string
>>> complex(3+9j)
(3+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(3)
True
>>> bool(4.7)
True
>>> bool("ammu")
True
>>> bool(3+9l)
SyntaxError: invalid decimal literal
>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(0)
False
