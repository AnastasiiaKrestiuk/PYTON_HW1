'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
'''

n = 385916

a = n%10
b = int(n/10)%10
c = int(n/100)%10
d = int(n/1000)%10
e = int(n/10000)%10
f = int(n/100000)

if((a+b+c) == (d+e+f)):
    print("yes")
else:
    print("no")