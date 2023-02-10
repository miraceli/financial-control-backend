from .models import *
from rest_framework import serializers


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['id','url','name','bank','type']

class CashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cash
        fields = ['id','url','name','valueReceivable','dateReceivable']

class CostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cost
        fields = ['id','url','name','valuePayable','datePayable']

class IncomeSerializer(serializers.HyperlinkedModelSerializer):
    cash_set = CashSerializer(many=True)
    class Meta:
        model = Income
        fields = ['id','url','name','cash_set']

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    cost_set = CostSerializer(many=True)
    class Meta:
        model = Expense
        fields = ['id','url','name','cost_set']