# Generated by Django 4.1.6 on 2023-02-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cost_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bank',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('C', 'Crédito'), ('D', 'Débito')], default='D', max_length=1),
        ),
    ]
