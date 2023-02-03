from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Account)
admin.site.register(Cash)
admin.site.register(Cost)