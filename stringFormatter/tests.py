import json

from django.test import TestCase

from .models import Text



class FormatterTests(TestCase):

    def test_to_upper_case(self):
        self.assertEquals(Text.to_upper_case("abcdefgh"), "ABCDEFGH")

    def test_to_upper_case_big(self):
        self.assertEquals(Text.to_upper_case("abcDefghijkLmnopqrstuvWXYz"), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_to_lower_case(self):
        self.assertEquals(Text.to_lower_case("ABCDEFGH"), "abcdefgh")

    def test_to_lower_case_big(self):
        self.assertEquals(Text.to_lower_case("ABCDEFGHijklMNOPQRStuvwxyZ"), "abcdefghijklmnopqrstuvwxyz")

class ViewTests(TestCase):

    def test_index_exists(self):
        index = self.client.get('/stringFormatter/')
        self.assertEquals(index.status_code, 200)

    def test_about_exists(self):
        index = self.client.get('/stringFormatter/about/')
        self.assertEquals(index.status_code, 200)

    def test_formatter_exists(self):
        index = self.client.get('/stringFormatter/formatter/')
        self.assertEquals(index.status_code, 200)

    def test_randomiser_exists(self):
        index = self.client.get('/stringFormatter/randomiser/')
        self.assertEquals(index.status_code, 200)

    def test_pdfeditor_exists(self):
        index = self.client.get('/stringFormatter/pdfeditor/')
        self.assertEquals(index.status_code, 200)
