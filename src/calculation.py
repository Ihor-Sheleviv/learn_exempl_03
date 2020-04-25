def calculation(goods, choice, code_out):
    """
    розрахунок при виборі товару
    :param goods:
    :param choice:
    :param code_out:
    :return: [goods, choice, warn]
    """
    warn = None
    d_choice = dict(choice)
    if len(code_out) > 0:
        code = code_out[0]
        number = code_out[1]
        amount =  code_out[2]
    else:
        return [goods, choice, None]

    n_goods = len(goods)
    """ нема товару нема про що балакати"""
    if n_goods == 0: return [[],[],None]
    """ підтвердили купівлю залишаємо як є"""
    if code == 1: return [goods,choice, None]
    """ увели шопопало замість номера """
    if code == 2: return [goods, choice, 'Error product']
    """ увели шопопало замість кількості """
    if code == 3: return [goods, choice, 'Error number']
    """ відмова від купівлі повертаємо все назад по кількості"""
    if code == -1:
        for n, commodity in enumerate(goods):
            amount = d_choice.get(commodity[0].strip(),0)
            if amount > 0:
                goods[n][2] = goods[n][2] + amount
        return [goods, [], None]
    """ підтверджено купівлю """
    if code == 1: return [goods, choice, None]

    """ нема такого номеру товару """
    if number > n_goods or number < 0: return [goods, choice, 'Not number product']
    """ відємна кількість товару у виборі """
    if amount < 0: return [goods, choice, 'Negative number']

    """ нульова кількість товару у виборі """
    if amount == 0:
        name_goods = goods[number - 1][0].strip()
        amount_goods = goods[number - 1][2]
        amount_ch = d_choice.get(name_goods, None)
        if amount_ch is None:
            # обрана кількість нульова
            return [goods, choice, 'Product enter zero']
        else:
            # корегуємо вибір, повертаємо товар
            goods[number - 1][2] = goods[number - 1][2] + amount_ch
            d_choice.pop(name_goods)
            warn = 'Product enter zero'
            choice = [[name_goods, amount] for name_goods, amount in d_choice.items()]
            return [goods, choice, warn]

    name_goods = goods[number-1][0].strip()
    amount_goods = goods[number-1][2]
    amount_ch = d_choice.get(name_goods, None)
    if amount_ch is None:
        # Товар раніше не вибирався (не корекція)
        if amount_goods >= amount:
            # товару достатньо
            d_choice[name_goods] = amount
            goods[number-1][2] = goods[number-1][2] - amount
        else:
            # товару менше ніж є
            d_choice[name_goods] = amount_goods
            goods[number-1][2] = 0
            warn = 'Product less'
    else:
        # корекція вибору
        if amount_goods + amount_ch >= amount:
            # товару достатньо
            d_choice[name_goods] = amount
            goods[number-1][2] = goods[number-1][2] + amount_ch - amount
            warn = 'Change the number'
        else:
            # товару менше ніж є
            d_choice[name_goods] = amount_goods + amount_ch
            goods[number-1][2] = 0
            warn = 'Product less'

    choice = [[name_goods, amount] for name_goods, amount in d_choice.items()]
    return [goods, choice, warn]