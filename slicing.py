Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
#slicing
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a[0:]
'codegnan'
b="work until you succeed"
b[6:11]
'ntil '
b[5:11]
'until '
b[12:15]
'ou '
b[11:15]
'you '
b[0:4]
'work'
b[16:23]
'ucceed'
b[15:23]
'succeed'
b="codegnan it solutions"
b[9:11]
'it'
b[0:8]
'codegnan'
b[12:20]
'solution'
#negative slicing
a="Vijayawada is a royal city"
a[-9:4]
''
a=[-9:-4]
SyntaxError: invalid syntax
c="Vijayawada is a royal city"
c=[-9:-4]
SyntaxError: invalid syntax
s="Vijayawada is a royal city"
s[-9:-4]
'oyal '
s[-10:-5]
'royal'
s[-26:-]16
SyntaxError: invalid syntax
s[-26:-16]
'Vijayawada'
s=[-4:-o]
SyntaxError: invalid syntax
s=[-4:0]
SyntaxError: invalid syntax
s=[-4:-1]
SyntaxError: invalid syntax
s=[-4:]
SyntaxError: invalid syntax
s[-4:]
'city'
d="vizag is city of destiny"
d[-26:-16]
'vizag is'
d[-7:]
'destiny'
d[-15:-11]
'city'
d[-24:-19]
'vizag'
#striding
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::2]
'Dt cec'
a[::4]
'D e'
a[1::2]
'aaSine'
a[1:3:2]
'a'
 c="Cloud Computing"
...  
SyntaxError: unexpected indent
>>> c="Cloud Computing"
>>> a[::5]
'DSc'
>>> c[::5]
'C u'
>>> c[::4]
'Cdmi'
>>> c[::8]
'Cm'
>>> c[2:]
'oud Computing'
>>> c[:9]
'Cloud Com'
>>> c[3:11]
'ud Compu'
>>> c[::2]
'CodCmuig'
>>> c[::6]
'CCi'
>>>  p="Python Course"
...  
SyntaxError: unexpected indent
>>> p="Python Course"
>>> a[-1:-10:-2]
'eniSa'
>>> p[-1:-10:-2]
'ero o'
>>> p[-3:-13:-4]
'r t'
>>> p[-5:-11:-3]
'on'
>>> e="machine learning"
>>> e[3:14:2]
'hn eri'
>>> e{5:15:4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> e{5:15:4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> e[5:15:4]
'nei'
>>> e[2:12:3]
'cnlr'
>>> e[0:10:1]
'machine le'
