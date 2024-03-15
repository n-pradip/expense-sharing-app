from django.db import models

class ExpenseCategory(models.Model):
    expense_name = models.CharField(max_length=128)
    description = models.TextField()


    def __str__(self):
        return self.expense_name