en = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./ "
ru = "ё1234567890-=йцукенгшщзхъфывапролджэячсмитьбю. "
res = ''

def ru_to_en():
    global res, en, ru

    for i in input():
        res += en[ru.index(i)]
    return res

def en_to_ru():
    global res, en, ru

    for i in input():
        res += ru[en.index(i)]
    return res

def start():
        a = input('0 : русская -> латинская, 1 : латинская -> русская\n')
        if a == '0':
            print(ru_to_en())
        elif a == '1':
            print(en_to_ru())
        else:
            print('Некорректный ввод!')
            start()

if __name__ == '__main__':
    start()
