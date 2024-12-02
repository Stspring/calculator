def add(a):
    for i in range(1, len(list_num)):
        list_num[0] += list_num[i]
    return  list_num[0]

def mul(a):
    for i in range(1, len(list_num)):
        list_num[0] *= list_num[i]
    return list_num[0]

def sub(a):
    for i in range(1, len(list_num)):
        list_num[0] -= list_num[i]
    return list_num[0] 

def div(a):
    for i in range(1, len(list_num)):
        list_num[0] /= list_num[i]
    return list_num[0]

def deg(a):
    for i in range(1, len(a)):
        a[0]  = a[0] ** a[i]
    return a[0]





print('Введите пример:')
example = input()
list_num = []

if '+' in example:
    example.replace(' ',' ')
    spl_ex = example.split('+')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = add(list_num)
elif '*' in example:
    example.replace(' ',' ')
    spl_ex = example.split('*')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = mul(list_num)
elif '-' in example:
    spl_ex = example.split('-')
    example.replace(' ',' ')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    print(list_num[1])
    result = sub(list_num)
elif '/' in example:
    spl_ex = example.split('/')
    example.replace(' ',' ')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = div(list_num)    
elif '**' in example:
    spl_ex = example.split('**')
    example.replace(' ',' ')
    list_ex = spl_ex
    len(list_ex)
    for i in range(len(list_ex)):
        list_num.append(float(list_ex[i]))
    result = deg(list_num)
print(result)