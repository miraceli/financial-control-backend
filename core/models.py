from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Income(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Account(models.Model):
    CREDIT = 'C'
    DEBIT = 'D'
    TYPE = [
        (CREDIT, 'Crédito'),
        (DEBIT, 'Débito'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bank = models.CharField(max_length=50,default="")
    type = models.CharField(max_length=1,choices=TYPE,default=DEBIT)

    def __str__(self):
        return self.name

class Cash(models.Model):
    name = models.CharField(max_length=50)
    valueReceivable = models.DecimalField(max_digits=10,decimal_places=2)
    dateReceivable = models.DateField(default=date.today)
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cost(models.Model):
    name = models.CharField(max_length=50)
    valuePayable = models.DecimalField(max_digits=10,decimal_places=2)
    datePayable = models.DateField(default=date.today)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    def __str__(self):
        return self.name