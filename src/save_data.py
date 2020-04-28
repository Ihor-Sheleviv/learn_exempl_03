class WrongFileData(Exception):
    """ відсутній файл з даними """
    pass

def save_data(goods, path, filename):
    """
    Записує дані про наявні товари у файл
    Перед записом робить резервну копію попереднього файлу
    із даними
    :param goods:
    :param path:
    :param filename:
    :return:
    """

    return 0