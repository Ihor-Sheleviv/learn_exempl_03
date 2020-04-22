def input_operation(dialog = True):
    """
    діалог із користувачем
    Користувач має увести номер товару й кількість товару
    Уведення Enter означає підтвердження вибраних товарів
    Уведення 0 означає відмову від вибору й придбання товарів
    :param dialog: = True Активізація діалогу
    :return: (код операції, номер товару, кількість товару)
    коди завершення:
    -1 уведено нульовий номер, завершити сеанс вибору
     0 нормальний вибір (числові дані не перевіряються)
     1 натиснуто Enter, вибір товарів завершено
     2 уведено нечислові дані в номері товару
     3 уведено нечислові дані в кількості товару
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
        else:
            return [2, 0, 0]

        s_data = input('Enter quantity of goods and key Enter ')
        if s_data.isdigit():
            value = int(s_data)
        else:
            return [3, 0, 0]

    return [code, number, value]