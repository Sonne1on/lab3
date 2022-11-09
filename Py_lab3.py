All_items = {
    'В': [3, 25, 0],#    Винтовка
    'П': [2, 15, 0],#    Пистолет
    'Б': [2, 15, 0],#    Боекомплект
    'А': [2, 10, 0],#    Аптечка
    'И': [1, 5, 1],#    Ингалятор
    'Н': [1, 15, 0],#    Нож
    'Т': [3, 20, 0],#    Топор
    'О': [1, 25, 0],#    Оберег
    'Ф': [1, 15, 0],#    Фляжка
    'Д': [1, 10, 1],#    Антидот
    'К': [2, 20, 0],#    Еда
    'Р': [2, 20, 0],#    Арбалет
}

# Разложим вещи по их ценности
def items_pl(items, max_sp):
    area = [items[item][0] for item in items]
    value = [items[item][1] for item in items]
    n = len(value)

    table = [[0 for a in range(max_sp + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(max_sp + 1):
            if i == 0 or a == 0:
                table[i][a] = 0

            elif area[i - 1] <= a:
                table[i][a] = max(value[i - 1] + table[i - 1][a - area[i - 1]], table[i - 1][a])

            else:
                table[i][a] = table[i - 1][a]
    print("Мест в рюкзаке: ", max_sp)
    return table, area, value

# Задаем начальные условия Вариант 4
# Ячейки 3х3=9
# Болезни нет
# Очки выживания 15

def items_pl_list(_items, max_sp = 9, sick='no'):
    items = {}
    if sick == 'no':
        for key, item in _items.items():
            if item[2] == 0:
                items[key] = item

    table, area, value = items_pl(items, max_sp)
    names = [key for key, value in items.items()]
    n = len(value)
    res = table[n][max_sp]
    max_result = res + 15
    a = max_sp
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][a]:
            continue
        else:
            items_list.append(names[i - 1])
            res -= value[i - 1]
            a -= area[i - 1]

    for key, item in items.items():
        if key not in items_list:
            max_result -= item[1]

    if max_result < 0:
        print("Нехватает очков выживания")
        return
    k = 0
    print("Выбраны вещи: ", items_list)
    print()
    while len(items_list) or k < 1:
        free = 3
        k += 1
        i = 0
        row = ''
        while i < len(items_list) or free > 0:
            item = items_list[i]
            if item:
                size = All_items[item][0]
                if size <= free:
                    row += f'[{item}],' * size
                    free -= size
                    items_list.remove(item)
                    i = 0
                else:
                    i += 1
        print(row)
    print()
    print("Очки выживания: ", max_result)
    return

items_pl_list(All_items)
