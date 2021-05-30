# Generated by Django 3.1 on 2020-08-23 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0007_order_proid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50, verbose_name='color')),
                ('size', models.CharField(max_length=50, verbose_name='size')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop1.product')),
            ],
        ),
    ]