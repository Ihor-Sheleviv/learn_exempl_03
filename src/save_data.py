import os

class WrongFileData(Exception):
    """ відсутній файл з даними """
    def __init__(self, message):
        super().__init__(message)

def my_write(fh, data):
    """ це для тестування виключень """
    return fh.write(data)


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
    if len(goods) == 0:
        return -1
    if not os.access(path+'\\'+filename, os.F_OK):
        raise WrongFileData('The machine does not work. Contact this admin!')

    try:
        os.replace(path+'\\'+filename, path+'\\'+filename[:-4]+'.dbk')
    except:
        raise WrongFileData('The machine does not work. Contact this admin!!')

    try:
        with open(path + '\\' + filename, 'w') as f:
            my_write(f,str(goods))
    except:
        raise WrongFileData('The machine does not work. Contact this admin!!')

    return 0