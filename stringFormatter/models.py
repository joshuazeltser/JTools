from django.db import models


class Text(models.Model):
    text_id = models.IntegerField(default=0, unique=True)
    text = models.CharField(max_length=1000)
    result = models.CharField(default=0, max_length=100)

    def __str__(self):
        return self.text
