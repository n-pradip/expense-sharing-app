from django.contrib import admin
from main.models import *

admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(ExpenseGroup)
admin.site.register(Settlement)