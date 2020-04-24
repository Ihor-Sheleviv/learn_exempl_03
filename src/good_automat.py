# -*- coding: utf-8 -*-
__author__ = "Ihor Shelevytsky"

from load_data import load_data
from display_info import display_info
from input_operation import input_operation
from calculation import calculation
from save_data import save_data
from save_story import save_story
from pay import pay


def good_automat():
    """ прототип роботи торгового автомата """
    while True:
        load_data('.','data.txt')
        display_info([],[])
        act = input_operation(False)
        calculation([],[],[])
        save_data()
        save_story()
        pay()
        break
        if act == 0:
            return 0

    return 0


if __name__ == "__main__":
    automat()
