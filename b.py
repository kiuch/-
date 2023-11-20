Python 3.11.5 | packaged by Anaconda, Inc. | (main, Sep 11 2023, 13:26:23) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[5,1,3,4]
print(a)
[5, 1, 3, 4]
print(a[0])
5
print(a[2])
3
a=[1]*4
a
[1, 1, 1, 1]
e= List()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    e= List()
NameError: name 'List' is not defined. Did you mean: 'list'?
n=List(range(5))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    n=List(range(5))
NameError: name 'List' is not defined. Did you mean: 'list'?
e=list
e=list()
n=list(range(5))
print(n)
[0, 1, 2, 3, 4]
s=list('abcde')
prnt(s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    prnt(s)
NameError: name 'prnt' is not defined. Did you mean: 'print'?
print(s))
SyntaxError: unmatched ')'
print(s)
['a', 'b', 'c', 'd', 'e']
t="a textbook of Python"
tlist=t.split()
print(tlist)
['a', 'textbook', 'of', 'Python']
a=[5,1,3,4]
print(a[0])
5
a[1]=2
print(a)
[5, 2, 3, 4]
print(len(a))
4
a=[5,1,3,4]
print(a[-1])
4
a=[5,1,3,4]
b=a[1:3]
print(b)
[1, 3]
a=[5,1,3,4]
a.append(2)
print(a)
[5, 1, 3, 4, 2]
a=[5,1,3,4]
b=[2,6]
a.extend(b)
print(a)
[5, 1, 3, 4, 2, 6]

a=[5,1,3,4]
b=[2,6]
a.append(b)
print(a)
SyntaxError: multiple statements found while compiling a single statement
a=[5,1,3,4]
b=[2,6]
a,append(b)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,append(b)
NameError: name 'append' is not defined
a.append(b)
print(a)
[5, 1, 3, 4, [2, 6]]
a=[1,2,3]
b=a
print(a)
[1, 2, 3]
print(b)
[1, 2, 3]
b[0]=0
a[1]=0
print(a)
[0, 0, 3]
print(b)
[0, 0, 3]
print(id(a),id(b))
3036335614208 3036335614208
b=a.copy
b=a.copy()
>>> a=1
>>> b=a
>>> b=2
>>> print(a,b)
1 2
>>> a=1
>>> b=a
>>> print(id(a),id(b))
140717794562856 140717794562856
>>> b=2
>>> print(id(a),id(b))
140717794562856 140717794562888
>>> a=[[1,2],[3,4]
...    ]
>>> b=a.copy
>>> b,append([5,6])
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    b,append([5,6])
NameError: name 'append' is not defined
>>> a=[[1,2],[3,4]]
>>> b=a.copy()
>>> b.appen([5,6])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    b.appen([5,6])
AttributeError: 'list' object has no attribute 'appen'. Did you mean: 'append'?
>>> b.append([5,6])
>>> print(a)
[[1, 2], [3, 4]]
>>> print(b)
[[1, 2], [3, 4], [5, 6]]
>>> b[0][0]=0
>>> print(a)
[[0, 2], [3, 4]]
>>> print(b)
[[0, 2], [3, 4], [5, 6]]
>>> print(id(a[0]),id(b[0]))
3036335583808 3036335583808
