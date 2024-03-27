from django.db import models
from accounts.models import User
class ExpenseCategory(models.Model):
    expense_name = models.CharField(max_length=128)
    description = models.TextField()


    def __str__(self):
        return self.expense_name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name="expense_category")
    date = models.DateField()
    receipt = models.ImageField(upload_to='receipts/', null=True, blank=True)
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    
class ExpenseGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User)
    
class Settlement(models.Model):
    expense_group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)
    payer = models.ForeignKey(User, related_name='payer', on_delete=models.CASCADE)
    payee = models.ForeignKey(User, related_name='payee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    settled = models.BooleanField(default=False)
