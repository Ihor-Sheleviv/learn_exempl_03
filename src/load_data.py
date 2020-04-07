import os


def load_data(path, filename):
    """
    завантаження даних про наявні товари
    :param path: шлях до файла
    :param filename: імя файла
    :return: [code, goods]
    code код результату 0-добре goods список товарів
    1 відсутній вказаний шлях
    2 відсутній вказаний файл
    21 помилка IOError під час читання
    3 вказаний файл пустий
    4 список товарів пустий []
    5 у файлі синтаксична помилка у списку SyntaxError
    6 у файлі невірні дані NameError
    26 список довший за 25 товарів

    todo функція не перевіряє чи це список
    todo функція не перевіряє правильність структури й значень списку
    """

    code = 0  # код завершення
    goods = []  # список товарів
    strlist = ''

    # перевіримо чи є такий шлях
    if not os.path.isdir(path):
        return [1, []]
    # перевіримо чи є такий файл
    if not os.path.isfile(path + '\\' + filename):
        return [2, []]
    # прочитаємо дані із файла
    try:
        with open(path + '\\' + filename, 'r') as f:
            strlist = f.read()
    except IOError:
        return [21, []]

    # якщо файл пустий
    if len(strlist) < 2:
        return [3, []]

    # перетворюємо рядок на список
    try:
        goods = eval(strlist)
    except SyntaxError:
        # синтаксична помилка
        return [5, []]
    except NameError:
        # якийсь невідомий ідентифікатор
        return [6, []]

    # todo а якщо це не список?
    #if not isinstance(goods, list):
    #    return [6,[]]
    # перевіримо довжину списку
    n = len(goods)
    if n == 0:
        return [4, []]
    if n > 25:
        code = 26
    # todo перевіряти помилки в списку

    return [code, goods]
