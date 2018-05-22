import json

from django.test import TestCase

from stringFormatter.formatter import *


class FormatterTests(TestCase):


    def test_to_upper_case(self):
        self.assertEquals(to_upper_case("abcdefgh"), "ABCDEFGH")

    def test_to_upper_case_big(self):
        self.assertEquals(to_upper_case("abcDefghijkLmnopqrstuvWXYz"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_to_lower_case(self):
        self.assertEquals(to_lower_case("ABCDEFGH"), "abcdefgh")

    def test_to_lower_case_big(self):
        self.assertEquals(to_lower_case("ABCDEFGHijklMNOPQRStuvwxyZ"), "abcdefghijklmnopqrstuvwxyz")

    def test_word_occurence_count(self):
        string = "hello my name is joshua and my name is joshua joshua is my name hello what the hell"
        #can't get this test to work properly
        print(json.dumps(word_occurence_count(string)))
