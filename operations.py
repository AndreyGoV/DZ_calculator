def calculator(act, num1, num2):
    result = 0
    if act == '+':
        result = num1 + num2
    elif act == '-':
        result = num1 - num2
    elif act == '*':
        result = num1 * num2
    elif act == '/':
        if num2 == 0:
            result = 'На 0 делить нельзя.'
        else:
            result = num1 / num2
    elif act == '^':
        result = num1 ** num2

    return result
