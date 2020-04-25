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

    return [goods, choice, warn]