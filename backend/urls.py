from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import *
from core.views import *
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'income', IncomeViewSet,basename='income')
router.register(r'expense', ExpenseViewSet,basename='expense')
router.register(r'account', AccountViewSet,basename='account')
router.register(r'cash', CashViewSet, basename='cash')
router.register(r'cost', CostViewSet, basename='cost')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token, name='login'),
    path('admin/', admin.site.urls),
]
