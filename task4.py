c = input('Введите число от 1 до 10:')
try:  
    v = int(c)
except ValueError:
    try:
        v = float(c)
    except ValueError:        
        v = 0 
        print('Не удается распознать')
print(v + 10)
#name = input('Введите ваше имя: ')
#print(f'Привет, {name}! Как дела?')