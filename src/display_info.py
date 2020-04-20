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

    d_choice = dict(choice)

    kadr = [' N|    goods                | num | price |choice|  value  ']
    if len(goods) == 0:
        empty = '  |                         |     |       |      |         \n'*25
        print(kadr[0])
        print(empty[:-1])
        print('                                     Cost |                ')
        print(' NOT GOODS                                                 ')
        return 0
    n = 1
    sum_ch = 0
    for good, price, num in goods:
        num_ch = d_choice.get(good.strip(),0)
        if  num_ch > 0:
            val_ch = num_ch * price
            sum_ch = sum_ch + val_ch
            kadr.append(f'{n:2}| {good:<24}|{num:5}|{price:7.2f}|{num_ch:6}|{val_ch:9.2f}')
        else:
            kadr.append(f'{n:2}| {good:<24}|{num:5}|{price:7.2f}|      |         ')
        n = n + 1

    if n < 25:
        empty = '  |                         |     |       |      |         \n' * (25-n+1)
        kadr.append(empty[:-1])
    if sum_ch>0:
        kadr.append(f'                                     Cost |{sum_ch:>16.2f}')
    else:
        kadr.append('                                     Cost |                ')
    if warning is None:
        kadr.append('                                                           ')
    else:
        kadr.append(f' {warning:<58}')

    for row in kadr:
        print(row)

    return 0
