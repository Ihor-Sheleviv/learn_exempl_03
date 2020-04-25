import unittest
from calculation import calculation

class TestCalculationOneCase(unittest.TestCase):
    """  тестуємо нормальний вибір одного товару  """
    def test_zero(self):
        """ все пусто """
        goods = []
        choice = []
        code_out = [0, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[],[], None])

    def test_one_one(self):
        """ один товар один вибіp """
        goods = [['good 1',10.00,20]]
        choice = []
        code_out = [0, 1, 2]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1',10.00,18]],[['good 1',2]], None])

    def test_one_one_less(self):
        """ вибрано товару більше ніж є """
        goods = [['good 1', 10.00, 2]]
        choice = []
        code_out = [0, 1, 3]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [ [['good 1', 10.00, 0]], [['good 1', 2]], 'Product less' ])

    def test_one_one_zero(self):
        """ вибрано нульову кількість """
        goods = [['good 1', 10.00, 2]]
        choice = []
        code_out = [0, 1, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 2]], [['good 1', 2]], 'Product enter zero'])

    def test_one_one_negative(self):
        """ вибрано негативну кількість """
        goods = [['good 1', 10.00, 2]]
        choice = []
        code_out = [0, 1, -2]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 2]], [['good 1',0]], 'Negative number'])

    def test_one_one_not(self):
        """ вибрано невірний номер товару """
        goods = [['good 1', 10.00, 2]]
        choice = []
        code_out = [0, 2, 1]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 2]], [], 'Not number product'])

    def test_one_one_change(self):
        """ один товар зміна кількості вибраного товару """
        goods = [['good 1', 10.00, 2]]
        choice = [['good 1', 3]]
        code_out = [0, 1, 1]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 4]], [['good 1', 1]], 'Change the number'])

    def test_one_one_change_less(self):
        """ зміна кількості, вибраного товару забагато """
        goods = [['good 1', 10.00, 2]]
        choice = [['good 1', 3]]
        code_out = [0, 1, 6]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 0]], [['good 1', 5]], 'Product less'])

    def test_one_one_end(self):
        """ завершення вибору товару """
        goods = [['good 1', 10.00, 2]]
        choice = [['good 1', 3]]
        code_out = [1, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 2]], [['good 1', 3]], None])

    def test_one_one_break(self):
        """ завершення відмова вибору """
        goods = [['good 1', 10.00, 2]]
        choice = [['good 1', 3]]
        code_out = [-1, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 5]], [], None])

    def test_one_nonumber_1(self):
        """ нечислові дані в номері товару """
        goods = [['good 1', 10.00, 2]]
        choice = [['good 1', 3]]
        code_out = [2, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 2],], [['good 1', 3],], 'Error product'])

    def test_one_nonumber_2(self):
        """ нечислові дані в кількості товару """
        goods = [['good 1', 10.00, 2]]
        choice = [['good 1', 3]]
        code_out = [3, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1', 10.00, 2],], [['good 1', 3],], 'Error number'])

class TestCalculationMoreCase(unittest.TestCase):
    """  тестуємо вибір декількох товарів  """
    def test_normal(self):
        """ вибір товару """
        goods = [['good 1',10.00,17],['good 2',12.00,30],
                 ['good 3',10.20,24],['good 4',10.04, 8],]
        choice = [['good 1', 3], ['good 3', 1]]
        code_out = [0, 4, 2]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1',10.00,17],['good 2',12.00,30],
                                  ['good 3',10.20,24],['good 4',10.04, 6],],
                                 [['good 1', 3], ['good 3', 1],
                                  ['good 4', 2],], None])
    def test_corected(self):
        """ корекція товару """
        goods = [['good 1',10.00,17],['good 2',12.00,30],
                 ['good 3',10.20,24],['good 4',10.04, 8],]
        choice = [['good 1', 3], ['good 3', 1]]
        code_out = [0, 1, 2]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1',10.00,18],['good 2',12.00,30],
                                  ['good 3',10.20,24],['good 4',10.04, 8],],
                                 [['good 1', 3], ['good 3', 1],], None])

    def test_enter(self):
        """ завершення вибору товару """
        goods = [['good 1',10.00,17],['good 2',12.00,30],
                 ['good 3',10.20,24],['good 4',10.04, 8],]
        choice = [['good 1', 3], ['good 3', 1]]
        code_out = [1, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1',10.00,17],['good 2',12.00,30],
                                  ['good 3',10.20,24],['good 4',10.04, 8],],
                                 [['good 1', 3], ['good 3', 1],], None])

    def test_break(self):
        """ відмова вибраних товарів """
        goods = [['good 1',10.00,17],['good 2',12.00,30],
                 ['good 3',10.20,24],['good 4',10.04, 8],]
        choice = [['good 1', 3], ['good 3', 1]]
        code_out = [-1, 0, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1',10.00,20],['good 2',12.00,30],
                                  ['good 3',10.20,25],['good 4',10.04, 8],], [], None])

    def test_corected_zero(self):
        """ відмова одного вибраного товару """
        goods = [['good 1',10.00,17],['good 2',12.00,30],
                 ['good 3',10.20,24],['good 4',10.04, 8],]
        choice = [['good 1', 3], ['good 3', 1]]
        code_out = [0, 1, 0]
        a = calculation(goods, choice, code_out)
        self.assertListEqual(a, [[['good 1',10.00,20],['good 2',12.00,30],
                                  ['good 3',10.20,25],['good 4',10.04, 8],],
                                 [['good 3', 1]], None])


if __name__ == '__main__':
    unittest.main()
