'''
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
'''
s = str(input())
sum1 = int(s[0]) + int(s[1]) + int(s[2])
sum2 = int(s[3]) + int(s[4]) + int(s[5])
if sum1 == sum2:
  print('Счастливый')
else:
    print('Обычный')