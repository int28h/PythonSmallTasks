'''
Имеется программа, код которой указан ниже.
Укажите, какие значения будут содержать списки в помеченных участках:

a = [1, 2, 3]
b = a
# значения списка b?

a[1] = 10
# значения списка b?

b[0] = 20
# значения списка a?

a = [5, 6]
# значения списка b?
'''
[1, 2, 3]
[1, 10, 3]
[20, 10, 3]
[20, 10, 3]

'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
'''
s = [ int(i) for i in input().split()]
res = 0 
l = len(s)-1
for i in range(0,l+1):
    res += s[i]
print(res)
