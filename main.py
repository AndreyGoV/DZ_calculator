from calc.operations import calculator
from calc.history import write_history

symbols = ("+", "-", "*", "/", "^")
print('Чтобы выйти из программы введите "e" (exit)')

while True:
    act = str(input(f'Выберите действие {symbols}: '))

    if act == 'e':
        break

    if act not in symbols:
        print('Выберите оператор из списка.')
        continue

    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))

    result = calculator(act, num1, num2)
    write_history(act, num1, num2, result)
    print(result)
