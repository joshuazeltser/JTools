from django.db import models


class Text(models.Model):
    text_id = models.IntegerField(default=0, unique=True)
    text = models.CharField(max_length=1000)
    result = models.CharField(default=0, max_length=100)

    def __str__(self):
        return self.text

    def to_upper_case(string):
        return string.upper()

    def to_lower_case(string):
        return string.lower()

    def reverse_string(string):
        return string[::-1]

    def word_count(string):
        words = string.split()

        return len(words)

    def char_count(string):
        return len(string)

    def split_string_by(string, char):
        return string.split(char)

    def word_occurence_count(string):
        words = string.split()

        dict = {}

        for x in range(0, len(words)):
            dict[words[x]] = words.count(words[x])

        return str(dict)
