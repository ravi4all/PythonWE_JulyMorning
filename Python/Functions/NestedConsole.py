Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def calc():
	x = 10
	y = 13
	return x+y, x-y, x/y, x*y

>>> calc()
(23, -3, 0.7692307692307693, 130)
>>> x = calc()
>>> x[0]
23
>>> type(x[0])
<class 'int'>
>>> def calc():
	def add():
		x = 10
		y = 12
		z = x + y
		return z
	return add

>>> calc()
<function calc.<locals>.add at 0x0000019459C416A8>
>>> def calc():
	def add():
		x = 10
		y = 12
		z = x + y
		return z
	return add()

>>> calc()
22
>>> def calc():
	def add():
		x = 10
		y = 12
		z = x + y
		return z
	return add

>>> calc()
<function calc.<locals>.add at 0x0000019457643E18>
>>> calc
<function calc at 0x0000019459C416A8>
>>> calc()()
22
>>> x = calc()
>>> x
<function calc.<locals>.add at 0x0000019457643E18>
>>> x()
22
>>> def calc():
	x = 10
	y = 12
	def add():
		z = x + y
		return z
	def sub():
		z = x - y
		return z
	return add, sub

>>> x = calc()
>>> type(x)
<class 'tuple'>
>>> x
(<function calc.<locals>.add at 0x0000019459C416A8>, <function calc.<locals>.sub at 0x0000019459C497B8>)
>>> x[0]
<function calc.<locals>.add at 0x0000019459C416A8>
>>> x[0]()
22
>>> calc()()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    calc()()
TypeError: 'tuple' object is not callable
>>> calc()[0]()
22
>>> def calc():
	x = 10
	y = 12
	def add():
		z = x + y
		return z
	def sub():
		z = x - y
		return z
	return add(), sub()

>>> x = calc()
>>> x
(22, -2)
>>> calc()[0]
22
>>> 
