'''
На вход программе подаются две матрицы, каждая в следующем формате: на первой строке два целых положительных числа n и m, 
разделенных пробелом - размерность матрицы. В следующей строке находится n*m целых чисел, разделенных пробелами - 
элементы матрицы. Подразумевается, что матрица заполняется построчно, то есть первые m чисел - первый ряд матрицы, 
числа от m+1 до 2m - второй, и т.д.

Напечатайте произведение матриц (XY)^T, если они имеют подходящую форму, или строку "matrix shapes do not match", 
если формы матриц не совпадают должным образом. 

В этот раз мы проделали за вас подготовительную работу по считыванию матриц 
(когда вы начнёте решать, этот код будет уже написан):

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)

 Несколько комментариев:

    map(f, iterable, …) — встроенная функция языка Python, возвращает результат поэлементного применения функции f 
	к элементам последовательности iterable; если f принимает несколько аргументов, то на вход должно быть подано 
	соответствующее число последовательностей: результатом map(f, x, y, z) будет итератор, возвращающий поочерёдно f(x[0], 
	y[0], z[0]), f(x[1], y[1], z[1]), f(x[2], y[2], z[2]) и так далее; результат применения f к очередному набору 
	аргументов вычисляется только тогда, когда требуется использовать этот результат, но не ранее, подробнее и короче 
	в справке;
	
    np.fromiter создаёт NumPy-массив из итератора, то есть заставляет итератор вычислить все доступные значения 
	и сохраняет их в массив;
	
    input() — встроенная функция языка Python, читает одну строку (последовательность символов вплоть до символа 
	переноса строки) из входного потока данных и возвращает её как строку;
	
    split() — метод класса string, возвращает список слов в строке (здесь слова — последовательности символов, 
	разделённые пробельными символами); принимает дополнительные аргументы, подробнее в справке.
	
Sample Input 1:

2 3
8 7 7 14 4 6
4 3
5 5 1 5 2 6 3 3 9 1 4 6

Sample Output 1:

[[ 82  96 108  78]
 [ 96 114 108  66]]

Sample Input 2:

2 3
5 9 9 10 8 9
3 4
6 11 3 5 4 5 3 2 5 8 2 2

Sample Output 2:

matrix shapes do not match
'''
import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)
Y = Y.T

if(x_shape[1] == y_shape[1]):
    print(X.dot(Y))
else: 
    print("matrix shapes do not match")