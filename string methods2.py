Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#escape sequence
#\n-new line
#\t-tab space
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:Prameela\nmobile:9392375637\tmailid:kandiprameela96@gmail.com\nsilver jubilee college"
print(b)
name:Prameela
mobile:9392375637	mailid:kandiprameela96@gmail.com
silver jubilee college
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
b="wait wait until you succeed"
b.replace("wait","wait")
'wait wait until you succeed'
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#upper
a="ammu"
a.upper()
'AMMU'
b="HI"
b.lower()
'hi'
c.capitalize()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c.capitalize()
NameError: name 'c' is not defined

c="python"
c.capitalize()
'Python'
'Python'
'Python'
a="python course"
a.title(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.title(a)
TypeError: str.title() takes no arguments (1 given)
a.title()
'Python Course'
a="python"
a.is upper()
SyntaxError: invalid syntax
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isdigit()
False
b="python course"
b.isalpha()
False
b="pythoncourse"
b.isalpha()
True
d="123456"
d.isdigit
<built-in method isdigit of str object at 0x00000289C315F060>
d.isdigit()
True
d.isalnum()
True
s="prameela132"
s.isalnum()
True
f="prameela@56"
f.isalnum()
False
False
False

a="hello world"

a.startwith("h")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.startwith("h")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("h")
True
a.endswith("n")
False
#strip
#lstrip,rstrip
a="         ammu              "
a.strip()
'ammu'
a.lstrip()
'ammu              '
a.rstrip()
'         ammu'
#split

a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vja"
b.split()
['i', 'am', 'in', 'vja']
#join
a="vij ja ya"
"".join(a)
'vij ja ya'
b="pra","mee","la"
"".join(b)
'prameela'
" ".join(b)
'pra mee la'
"k".join(a)
'vkikjk kjkak kyka'
a="hello"
b="world"
print(a+" "+b)
hello world
a="pramela"

fname="prameela"
lname="kandi"
print(fname+" "+lname)
prameela kandi
print((fname+" "+lname).title())
Prameela Kandi
#formatting
a="4
SyntaxError: unterminated string literal (detected at line 1)
>>> a=4
>>> b=3
>>> print(a+b)
7
>>> print("the sum is",a+b)
the sum is 7
>>> v="vija
SyntaxError: unterminated string literal (detected at line 1)
>>> v="vja"
>>> print("hello",v)
hello vja
>>> #format method
>>> a="motu"
>>> b+"patlu"
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    b+"patlu"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> b="patlu"
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fstring
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> a=4
>>> b=6
>>> print(f"the product is {a}+{b}".format(a,b))
the product is 4+6
>>> print(f"the product is {a+b}".format(a,b))
the product is 10
>>> print(f"the product is {a*b}".format(a,b))
the product is 24
>>>  print(f"the product is {a*b}")
...  
SyntaxError: unexpected indent
>>> print(f"the product is {a*b}")
the product is 24
