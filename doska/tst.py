#!/usr/bin/env python
# -*- coding:utf-8 -*-
print 'Helllloooo'
arr = '1,2,3,4,5,2,3,4'.split(',') # указали по какому знаку разделить массив
print arr[1:3] # вывести знаки от их индекса с 0
print '-'.join(arr) # соединить символы массива через какой-то знак

print 'one2tree'.replace('2','5') # заменить любой знак, слово и т.д. на другой (2 заменяется на 5)
arr1='Дима, Юра, Вся'
arr2=arr1.replace('Юра','Петя')
print arr2
arr[0] = [1,2,3]

for i in arr:
    print '%s - number - %s' % (i,i)

print len(arr) # len вычсляет кол-во знаков в переменной, массиве, строке...

dict = {'title': 1, '1': 'title'} # Словарь - пара - ключ:значение
print dict['title']

per1 = 'Nata'
per2 = 'Viktor'

print '%s %f' % (per1,3.6) # %s - будет выводится символ как строка, %d - будет выводится десятичное, %f - floa


konvert=5
konvert2='6'
konvert3 = 5 + int(konvert2) # превратить элемент в число int
print konvert3
konvert4 = str(konvert) + konvert2 # превратить элемент в строку str
print konvert4


matr='1,2,3,4'.split(',')
print matr
matr[0]=[1,2,3,4]
print matr[0:2]

twoo=bin(9)
print twoo