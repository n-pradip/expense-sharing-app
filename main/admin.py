from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(ExpenseGroup)
admin.site.register(Group)
admin.site.register(Settlement)