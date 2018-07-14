Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/Python_WE_Morning/Loops/ForLoopDemo.py 
Value of i is 0
Still Inside For loop
Value of i is 1
Still Inside For loop
Value of i is 2
Still Inside For loop
Value of i is 3
Still Inside For loop
Value of i is 4
Still Inside For loop
Value of i is 5
Still Inside For loop
Value of i is 6
Still Inside For loop
Value of i is 7
Still Inside For loop
Value of i is 8
Still Inside For loop
Value of i is 9
Still Inside For loop
Outside for loop
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/Python_WE_Morning/Loops/ForLoopDemo.py 
Value of i is 5
Still Inside For loop
Value of i is 6
Still Inside For loop
Value of i is 7
Still Inside For loop
Value of i is 8
Still Inside For loop
Value of i is 9
Still Inside For loop
Outside for loop
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/Python_WE_Morning/Loops/PrintingTables.py 
5
10
15
20
25
30
35
40
45
50
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/July_2018/Python_WE_Morning/Loops/PrintingTables.py 
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
>>> import turtle
>>> eddy = turtle.Pen()
>>> eddy.shape('turtle')
>>> eddy.forward(200)
>>> eddy.left(90)
>>> eddy.forward(200)
>>> eddy.left(90)
>>> eddy.forward(200)
>>> eddy.left(90)
>>> eddy.forward(200)
>>> eddy.left(90)
>>> eddy.reset()
>>> for i in range(4):
	eddy.forward(200)
	eddy.left(90)

	
>>> eddy.reset()
>>> for i in range(4):
	eddy.forward(200)
	eddy.left(90)

	
>>> eddy.reset()
>>> for i in range(4):
	eddy.forward(200)
	eddy.left(90*i)

	
>>> eddy.reset()
>>> for i in range(4):
	eddy.forward(200)
	eddy.left(45*i)

	
>>> eddy.reset()
>>> for i in range(4):
	eddy.forward(20)
	eddy.left(45*i)

	
>>> eddy.reset()
>>> for i in range(10):
	eddy.forward(80)
	eddy.left(45*i)

	
>>> eddy.reset()
>>> for i in range(10):
	eddy.forward(8*i)
	eddy.left(90)

	
>>> eddy.reset()
>>> for i in range(30):
	eddy.forward(8*i)
	eddy.left(90)

	
>>> eddy.reset()
>>> for i in range(30):
	eddy.circle(30)
	eddy.left(45*i)

	
>>> eddy.reset()
>>> for i in range(30):
	eddy.circle(10*i)
	eddy.left(45)

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    eddy.circle(10*i)
  File "C:\Python36\lib\turtle.py", line 1992, in circle
    self.speed(0)
  File "C:\Python36\lib\turtle.py", line 2174, in speed
    self.pen(speed=speed)
  File "C:\Python36\lib\turtle.py", line 2459, in pen
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> eddy.reset()
>>> for i in range(30):
	eddy.circle(5*i)
	eddy.left(45*i)

	
Traceback (most recent call last):
  File "<pyshell#45>", line 3, in <module>
    eddy.left(45*i)
  File "C:\Python36\lib\turtle.py", line 1699, in left
    self._rotate(angle)
  File "C:\Python36\lib\turtle.py", line 3276, in _rotate
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> eddy.reset()
>>> eddy.speed(0)
>>> for i in range(60):
	eddy.circle(5*i)
	eddy.left(45)

	
>>> 
