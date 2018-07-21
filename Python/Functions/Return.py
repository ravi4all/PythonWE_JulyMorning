Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	z = x + y
	print(z)

	
>>> add(12,3)
15
>>> def showResult():
	a = add(2,3)
	print(a)

	
>>> showResult()
5
None
>>> a = add(2,3)
5
>>> print(a)
None
>>> def player_1():
	health = 80

	
>>> def player_2():
	health = 87

	
>>> def showHealth():
	p_1 = player_1()
	p_2 = player_2()
	print("Health of player_1",p_1)
	print("Health of player_2",p_2)

	
>>> showHealth()
Health of player_1 None
Health of player_2 None
>>> def player_1():
	health = 80
	return health

>>> def player_2():
	health = 87
	return health

>>> showHealth()
Health of player_1 80
Health of player_2 87
>>> p_1 = player_1()
>>> p_1
80
>>> 
