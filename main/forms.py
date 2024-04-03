from django import forms
from .models import *

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ['expense_name', 'description']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'category', 'date', 'receipt']


class ExpenseGroupForm(forms.ModelForm):
    class Meta:
        model = ExpenseGroup
        fields = '__all__'

class SettlementForm(forms.ModelForm):
    class Meta:
        model = Settlement
        fields = ['expense_group', 'payer', 'payee', 'amount', 'settled']
