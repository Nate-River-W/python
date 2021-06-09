from random import randint as r

Symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-'

count = int(input('Введите число символов: '))
a = 0
b = ''

def get_pass():
    password = ''
    for i in range(count):
        password = password + Symbols[r(0, len(Symbols) - 1)]
    return (f' {a}. {password}')

# for func in range(10):
#     get_pass()
#     a += 1

while 'Near' not in b:
    get_pass()
    b = get_pass()
    a += 1
    print(b)