'''
Задание №1: Перевод и 10 систему в 2
	def binary(number):
	    result = ''
	    if not number: 
	    	return '0'
	    while number !=0:
	       modulo = number % 2
	       number = number // 2
	       result = result + str(modulo)
	       
	       if number > 0:
	           continue
	       else:
	           result = result[::-1]
	           print(result) #result
	binary(0)
'''