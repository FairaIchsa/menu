from django.db import models


class MenuTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Item(models.Model):
    menu_title = models.ForeignKey(MenuTitle, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('Item', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

