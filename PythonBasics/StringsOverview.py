Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "hello this is python"
>>> len(a)
20
>>> a[0]
'h'
>>> a[2]
'l'
>>> a[-1]
'n'
>>> a[0:5]
'hello'
>>> a[0:4]
'hell'
>>> a[:]
'hello this is python'
>>> a[0:]
'hello this is python'
>>> a[:100]
'hello this is python'
>>> a[5:9]
' thi'
>>> a[0:17:2]
'hloti spt'
>>> a.capitalize()
'Hello this is python'
>>> a.upper()
'HELLO THIS IS PYTHON'
>>> a.find('p')
14
>>> b = a[14:]
>>> b
'python'
>>> a[0:17:3]
'hltssy'
>>> b
'python'
>>> b[::-1]
'nohtyp'
>>> a = "hello this is python programming"
>>> a.find('i')
8
>>> a.rfind('i')
29
>>> a.find('i',9)
11
>>> a.upper("hello")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.upper("hello")
TypeError: upper() takes no arguments (1 given)
>>> a.replace("hello","HELLO")
'HELLO this is python programming'
>>> a
'hello this is python programming'
>>> a[0] = 'X'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[0] = 'X'
TypeError: 'str' object does not support item assignment
>>> b
'python'
>>> b*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
>>> 20*10
200
>>> '20'*10
'20202020202020202020'
>>> s = 'I don't know python'
SyntaxError: invalid syntax
>>> s = "I don't know python"
>>> s = "Hello "world""
SyntaxError: invalid syntax
>>> s = 'Hello "world"'
>>> print(s)
Hello "world"
>>> 
