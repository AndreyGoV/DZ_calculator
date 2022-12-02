def write_history(act, num1, num2, result):
    f = open('result.txt', 'ta')
    f.write(f'{num1} {act} {num2} = {result}\n')

    f.close()