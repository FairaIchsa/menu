# Generated by Django 4.1.9 on 2023-05-07 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='menu_title',
            field=models.ForeignKey(blank=True, help_text='Is necessary when Parent field is None.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='mainapp.menutitle'),
        ),
    ]
