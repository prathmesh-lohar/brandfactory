# Generated by Django 3.1 on 2020-08-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0005_auto_20200818_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qnt',
        ),
        migrations.AddField(
            model_name='order',
            name='qnt',
            field=models.CharField(default='', max_length=50, verbose_name='qnt'),
        ),
    ]