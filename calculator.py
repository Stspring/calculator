n1 = int(input('Введите первое число'))
n2 = int(input('Введите второе число'))
def sum (n1,n2):
    return n1 + n2
def sub (n1, n2):
    return n1 - n2
def div (n1,n2):
    return n1 / n2
def mul (n1,n2):
    return n1 * n2
def calculator(n1, n2, operation):
    result = None
    if operation == '+':
        result = sum(n1, n2)
    elif operation == '-':
        result = sub(n1, n2)
    elif operation == '/':
        result = div(n1, n2)
    elif operation == '*':
        result = mul(n1,n2)
def operation():
    mes = input ('Выберите операцию (Введите +, -, /, *)','+ -сложение двух чисел',
                '- -вычитание двух чисел','/ -умножение двух чисел','* -деление двух чисел')
    
















































































     