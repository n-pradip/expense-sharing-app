from django.shortcuts import render, redirect, get_object_or_404
from main.models import ExpenseCategory
from .forms import ExpenseCategoryForm

def home(request):
    context={}
    return render(request,'home.html',context)


def expense_category_list(request):
    categories = ExpenseCategory.objects.all()
    return render(request, 'expense_category_list.html', {'categories': categories})

def expense_category_create(request):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_category_list')
    else:
        form = ExpenseCategoryForm()
    return render(request, 'expense_category_form.html', {'form': form})

def expense_category_update(request, pk):
    category = get_object_or_404(ExpenseCategory, pk=pk)
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('expense_category_list')
    else:
        form = ExpenseCategoryForm(instance=category)
    return render(request, 'expense_category_form.html', {'form': form})

def expense_category_delete(request, pk):
    category = get_object_or_404(ExpenseCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('expense_category_list')
    return render(request, 'expense_category_confirm_delete.html', {'category': category})
