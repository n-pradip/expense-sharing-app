from django.shortcuts import render
from main.models import ExpenseCategory

def expensecategory_views(request):
    objs = ExpenseCategory.objects.all()
    context={
        "expense_cat": objs,
    }
    return render(request,'expense_category.html',context)

def home(request):
    context={}
    return render(request,'home.html',context)
