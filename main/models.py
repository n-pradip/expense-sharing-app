from django.db import models
from accounts.models import User
from django.db.models import Q
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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by",null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.name} >>>  {self.amount}"
    
class ExpenseGroup(models.Model):
    group_name = models.CharField(max_length=100,null=True, blank=True)
    # group_mimic_name = models.CharField(max_length=128,null=True,blank=True  )
    members = models.ManyToManyField(User)
    # expense = models.ForeignKey(Expense, on_delete=models.CASCADE,null=True, blank=True)
    # assigned_to = models.ManyToManyField(User,related_name='assigned_to')
    def __str__(self):
        return self.group_name
    
class Settlement(models.Model):
    expense_group = models.ForeignKey(ExpenseGroup, on_delete=models.CASCADE)  # Update related name here
    payer = models.ForeignKey(User, related_name='payer', on_delete=models.CASCADE)
    payee = models.ForeignKey(User, related_name='payee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    settled = models.BooleanField(default=False)
    is_payement_done = models.BooleanField(default=False, null=True,blank=True)

    def __str__(self):
        return f"payer:{self.payer} payee: {self.payee}"