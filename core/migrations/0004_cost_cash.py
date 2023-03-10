# Generated by Django 4.1.6 on 2023-02-03 14:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('valuePayable', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datePayable', models.DateField(default=datetime.date.today)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.expense')),
            ],
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('valueReceivable', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dateReceivable', models.DateField(default=datetime.date.today)),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.income')),
            ],
        ),
    ]