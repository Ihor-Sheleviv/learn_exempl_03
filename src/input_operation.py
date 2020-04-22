def input_operation(dialog = True):
    """
    діалог із користувачем
    Користувач має увести номер товару й кількість товару
    Уведення Enter означає підтвердження вибраних товарів
    Уведення 0 означає відмову від вибору й придбання товарів
    :return: (код операції, номер товару, кількість товару)
    """
    code = 0
    number = 0
    value = 0
    if dialog:
        s_data = input('Enter item number and key Enter or ' +
                       'Enter - continue or zero - break ')
        if len(s_data) == 0:
            return [1, 0, 0]
        if s_data.isdigit():
            number = int(s_data)
            if number == 0:
                return [-1, 0, 0]

    return [code, number, value]