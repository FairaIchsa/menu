from django.db import models


class Item(models.Model):
    parent = models.ForeignKey('Item', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
