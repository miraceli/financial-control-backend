from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from core.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'account', AccountViewSet)
router.register(r'cash', CashViewSet)
router.register(r'cost', CostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
