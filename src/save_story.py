import datetime
from shutil import copyfile

class WrongFileStory(Exception):
    """ проблема з файлом історії """
    def __init__(self, message):
        super().__init__(message)

def my_write(fh, data):
    """ це для тестування виключень """
    return fh.write(data)

def save_story(data, path, filename):
    """
    зберегти історію дій з товарами
    :param data:
    :param path:
    :param filename:
    :return:
    """

    if filename == None:
        return 0

    try:
        copyfile(path+'\\'+filename, path+'\\'+filename[:-4]+'.dbk')
    except:
        raise WrongFileStory('The machine does not work. Error 101. Contact this admin!')

    data_str = str(data)
    today = datetime.datetime.today()
    info = today.strftime("%Y-%m-%d-%H.%M.%S") + ' ' + data_str + '\n'
    try:
        with open(path + '\\' + filename, 'a') as f:
            my_write(f,info)
    except:
        raise WrongFileStory('The machine does not work. Error 102. Contact this admin!')

    return 0