import unittest
import sys
import math
import re

from main import wybierz_sowe_zwroc_koszt
from main import licz_sume

class TestStringMethods(unittest.TestCase):
    #test zad4
    def test_good_costs(self):
        potwierdzenie_odbioru = True
        odleglosc = "lokalna"
        typ = "list"
        specjalna = None
        costs_result_expected = "{'galeon': 0, 'sykl': 0, 'knut': 9}"
        output_dict = wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna)
        costs_result_real = str(output_dict)

        self.assertEqual(costs_result_expected, costs_result_real)

    def test_bad_costs(self):
        potwierdzenie_odbioru = True
        odleglosc = "lokalna"
        typ = "list"
        specjalna = None
        costs_result_expected = "{'galeon': 0, 'sykl': 0, 'knut': 0}"
        output_dict = wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna)
        costs_result_real = str(output_dict)

        self.assertNotEqual(costs_result_expected, costs_result_real)

    def test_licz_sume():
        wejscie = [15,"galeon", 7, "knut", 98, "sykl"]
        slownik = {"galeon": 15, 
	    "sykl": 98,
	    "knut": 7}

    assert waluta_str_na_dict(wejscie) == slownik


'''
zeby dodac wiecej testow skopiuj def w obrebie klasy TestStringMethods.
Ja tutaj zrobilem sobie dwa testy, ty mozesz jeden.
'''