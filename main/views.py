from django.shortcuts import render, redirect, get_object_or_404
from .models import ExpenseGroup
from .forms import ExpenseGroupForm
from django.shortcuts import render, redirect, get_object_or_404
from main.models import ExpenseCategory
from .forms import *
from main.models import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = request.user
    expenses = Expense.objects.filter(user=user)
    expense_groups = ExpenseGroup.objects.filter(members=user)
    
    # Query for settlements where the user is either the payer or the payee
    settlements = Settlement.objects.filter(Q(payer=user) | Q(payee=user))
    
    context = {
        'user': user,
        'expenses': expenses,
        'expense_groups': expense_groups,
        'settlements': settlements,
    }
    return render(request, 'home.html', context)


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

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('homepage')
    else:
        form = ExpenseForm()
    return render(request, 'expense_create.html', {'form': form})

@login_required
def expense_edit(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_edit.html', {'form': form, 'expense': expense})

@login_required
def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('homepage')
    return render(request, 'expense_confirm_delete.html', {'expense': expense})



@login_required
def expense_group_list(request):
    expense_groups = Settlement.objects.all()
    return render(request, 'expense_groups_list.html', {'expense_groups': expense_groups})


@login_required
def expense_group_create(request):
    if request.method == 'POST':
        form = ExpenseGroupForm(request.POST)
        if form.is_valid():
            expense_group = form.save()
            return redirect('expense_group_detail', expense_group_id=expense_group.id)
    else:
        form = ExpenseGroupForm()
    return render(request, 'expense_group_create.html', {'form': form})

@login_required
def expense_group_detail(request, expense_group_id):
    expense_group = get_object_or_404(ExpenseGroup, id=expense_group_id)
    return render(request, 'expense_group_detail.html', {'expense_group': expense_group})

@login_required
def expense_group_edit(request, expense_group_id):
    expense_group = get_object_or_404(ExpenseGroup, id=expense_group_id)
    if request.method == 'POST':
        form = ExpenseGroupForm(request.POST, instance=expense_group)
        if form.is_valid():
            form.save()
            return redirect('expense_group_detail', expense_group_id=expense_group.id)
    else:
        form = ExpenseGroupForm(instance=expense_group)
    return render(request, 'expense_group_edit.html', {'form': form, 'expense_group': expense_group})

@login_required
def expense_group_delete(request, expense_group_id):
    expense_group = get_object_or_404(ExpenseGroup, id=expense_group_id)
    if request.method == 'POST':
        expense_group.delete()
        return redirect('homepage')
    return render(request, 'expense_group_confirm_delete.html', {'expense_group': expense_group})


@login_required
def settlement_create(request):
    if request.method == 'POST':
        form = SettlementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SettlementForm()
    return render(request, 'settlement_create.html', {'form': form})

@login_required
def settlement_edit(request, settlement_id):
    settlement = get_object_or_404(Settlement, id=settlement_id)
    if request.method == 'POST':
        form = SettlementForm(request.POST, instance=settlement)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SettlementForm(instance=settlement)
    return render(request, 'settlement_edit.html', {'form': form, 'settlement': settlement})

@login_required
def settlement_delete(request, settlement_id):
    settlement = get_object_or_404(Settlement, id=settlement_id)
    if request.method == 'POST':
        settlement.delete()
        return redirect('homepage')
    return render(request, 'settlement_confirm_delete.html', {'settlement': settlement})

@login_required
def settlement_list(request):
    settlements = Settlement.objects.all()
    return render(request, 'settlement_list.html', {'settlements': settlements})

@login_required
def search_expense_category(request):
    form = ExpenseCategoryFilterForm(request.GET or None)
    items = []
    
    if form.is_valid():
        title_query = form.cleaned_data.get('expense_name')
        if title_query:
            items = ExpenseCategory.objects.filter(expense_name__icontains=title_query)
    
    context = {
        'form': form,
        'items': items,
    }
    return render(request, 'search.html', context)