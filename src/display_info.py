def display_info(goods, choice, warning=None):
    """
    відображення наявних та обраних товарів на екрані
    можливі різні варіанти відображення залежно від типу дисплея
    найпростіший чорно-білий текстовий варіант із 24 рядками й 80 символами в рядку
    можливі й інші варіанти як то три рядки із 40 символами, або
    повноцінний графічний кольоровий дисплей.

    :param goods: наявні товари
    :param choice: товари вибрані покупцем
    :param warning: повідомлення покупцеві (опція)
    :return: """

    kadr = [' N|    goods                | num | price |choice|  value  ']
    if len(goods) == 0:
        empty = '  |                         |     |       |      |         \n'*25
        print(kadr[0])
        print(empty[:-1])
        print('                                     Cost |                ')
        print(' NOT GOODS                                                 ')
        return 0
    n = 1
    for good, price, num in goods:
        kadr.append(f'{n:2}| {good:<24}|{num:5}|{price:7.2f}|      |         ')
        n = n + 1

    if n < 25:
        empty = '  |                         |     |       |      |         \n' * (25-n+1)
        kadr.append(empty[:-1])
    kadr.append('                                     Cost |                ')
    kadr.append('                                                           ')

    for row in kadr:
        print(row)

    return 0
