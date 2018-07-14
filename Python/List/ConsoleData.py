Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> data = ['hello','hi',12,34,56,78,11,16,10.5,12.8]
>>> len(data)
10
>>> data[0]
'hello'
>>> data[5]
78
>>> data[-1]
12.8
>>> data[0:5]
['hello', 'hi', 12, 34, 56]
>>> data[:2]
['hello', 'hi']
>>> data[2:]
[12, 34, 56, 78, 11, 16, 10.5, 12.8]
>>> data[:]
['hello', 'hi', 12, 34, 56, 78, 11, 16, 10.5, 12.8]
>>> data[-1]
12.8
>>> data[:-1]
['hello', 'hi', 12, 34, 56, 78, 11, 16, 10.5]
>>> data = ['hello','hi',12,34,56,78,11,16,10.5,12.8,100,10,,102,105,19]
SyntaxError: invalid syntax
>>> data = ['hello','hi',12,34,56,78,11,16,10.5,12.8,100,10,102,105,19]
>>> data[0:10:2]
['hello', 12, 56, 11, 10.5]
>>> odd = []
>>> for i in range(1,50):
	if i % 2 == 0:
		odd.append(i)

		
>>> odd
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> odd.clear()
>>> odd
[]
>>> for i in range(1,50):
	if i % 2 != 0:
		odd.append(i)

		
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> odd.pop()
49
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
>>> for num in odd:
	if num == 17:
		print("Found")

		
Found
>>> for num in odd:
	if num == 18:
		print("Found")

		
>>> for i in range(len(odd)):
	if odd[i] == 17:
		print("Found at",i,"index")

		
Found at 8 index
>>> len(odd)
24
>>> for i in range(len(odd)):
	if odd[i] == 17:
		print("Found at",i,"index")
		break
	else:
		print("Not found yet...")

		
Not found yet...
Not found yet...
Not found yet...
Not found yet...
Not found yet...
Not found yet...
Not found yet...
Not found yet...
Found at 8 index
>>> 17 in odd
True
>>> odd.index(17)
8
>>> for i,num in enumerate(odd):
	if num == 18:
		print("Found at",i)
	else:
		print("Not found till",i)

		
Not found till 0
Not found till 1
Not found till 2
Not found till 3
Not found till 4
Not found till 5
Not found till 6
Not found till 7
Not found till 8
Not found till 9
Not found till 10
Not found till 11
Not found till 12
Not found till 13
Not found till 14
Not found till 15
Not found till 16
Not found till 17
Not found till 18
Not found till 19
Not found till 20
Not found till 21
Not found till 22
Not found till 23
>>> for i,num in enumerate(odd):
	if num == 17:
		print("Found at",i)
		break
	else:
		print("Not found till",i)

		
Not found till 0
Not found till 1
Not found till 2
Not found till 3
Not found till 4
Not found till 5
Not found till 6
Not found till 7
Found at 8
>>> for i, num in enumerate(odd):
	print(i,num)

	
0 1
1 3
2 5
3 7
4 9
5 11
6 13
7 15
8 17
9 19
10 21
11 23
12 25
13 27
14 29
15 31
16 33
17 35
18 37
19 39
20 41
21 43
22 45
23 47
>>> odd.pop(8)
17
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
>>> odd.remove(19)
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
>>> odd.index(15)
7
>>> odd.insert(8,17)
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
>>> odd.append(49)
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> odd_1 = [i for i in range(51,100)]
>>> odd_1
[51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> odd_1 = [i for i in range(51,100) if i % 2 != 0]
>>> odd_1
[51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> odd.append(odd_1)
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, [51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]]
>>> odd.pop()
[51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> odd.extend(odd_1)
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> numbers = []
>>> odd = [i for i in range(1,50) if i % 2 == 0]
>>> even = [i for i in range(1,50) if i % 2 == 0]
>>> odd = [i for i in range(1,50) if i % 2 != 0]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> numbers.append([odd,even])
>>> numbers
[[[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]]]
>>> numbers.clear()
>>> numbers.append(odd)
>>> numbers.append(even)
>>> numbers
[[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]]
>>> numbers[0]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> numbers[1]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> numbers[0][-1]
49
>>> numbers.clear()
>>> numbers.extend(odd)
>>> numbers.extend(evn)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    numbers.extend(evn)
NameError: name 'evn' is not defined
>>> numbers.extend(even)
>>> numbers
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> sorted(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> sorted(numbers, reverse = True)
[49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
