from django.db import models
from django.core.exceptions import ValidationError


class MenuTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Item(models.Model):
    menu_title = models.ForeignKey(MenuTitle, related_name='items', on_delete=models.CASCADE, null=True, blank=True,
                                   help_text='Is necessary when Parent field is None.')
    parent = models.ForeignKey('Item', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def clean(self):
        if self.parent is None and self.menu_title is None:
            raise ValidationError('The item should have Parent or Menu title')

    def save(self, *args, **kwargs):
        root = self
        while root.parent:
            root = root.parent
        self.menu_title = root.menu_title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

