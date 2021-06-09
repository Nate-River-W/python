listt = ['2','3','4']
number = input('Введите число: ')

if number[-1] == ('1'):
	print(number + ' Яблоко')
elif number[-1] in listt:
	print(number + ' Яблока')
else:
	print(number + ' Яблоко')
