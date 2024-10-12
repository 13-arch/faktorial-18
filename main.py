'''Требуется вычислить факториал целого числа N. Факториал обозначают как N! и вычисляют по формуле:

N! = 1 * 2 * 3 * … * (N-1) * N, причем 0!= 1.

Так же допустимо рекуррентное соотношение: N! = (N-1)! * N

Входные данные
В единственной строке входного файла INPUT.TXT записано одно целое неотрицательное число N (N < 1000).

Выходные данные
В выходной файл OUTPUT.TXT нужно вывести одно целое число — значение N!.'''
input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
a=int(data)
factorial = 1
for i in range(2, a+1):
    factorial *= i
output_data.write(str(factorial))
output_data.close()
input_data.close()