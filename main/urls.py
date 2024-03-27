from django.urls import path
from accounts.views import register,user_login,user_logout
from main import views
urlpatterns = [
    path('accounts/login/', user_login ,name="login"),
    path('register', register ,name="register"),
    path('logout', user_logout,name="logout"),
    path('',views.home,name="homepage"),
    path('category/list', views.expense_category_list, name='expense_category_list'),
    path('category/create/', views.expense_category_create, name='expense_category_create'),
    path('category/update/<int:pk>/', views.expense_category_update, name='expense_category_update'),
    path('category/delete/<int:pk>/', views.expense_category_delete, name='expense_category_delete'),

    path('expense/create/', views.expense_create, name='expense_create'),
    path('expense/<int:expense_id>/edit/', views.expense_edit, name='expense_edit'),
    path('expense/<int:expense_id>/delete/', views.expense_delete, name='expense_delete'),
    path('group/create/', views.group_create, name='group_create'),
    path('group/<int:group_id>/edit/', views.group_edit, name='group_edit'),
    path('group/<int:group_id>/delete/', views.group_delete, name='group_delete'),
    path('expensegroup/create/', views.expense_group_create, name='expense_group_create'),
    path('expensegroup/<int:expense_group_id>/edit/', views.expense_group_edit, name='expense_group_edit'),
    path('expensegroup/<int:expense_group_id>/delete/', views.expense_group_delete, name='expense_group_delete'),
    path('settlement/create/', views.settlement_create, name='settlement_create'),
    path('settlement/<int:settlement_id>/edit/', views.settlement_edit, name='settlement_edit'),
    path('settlement/<int:settlement_id>/delete/', views.settlement_delete, name='settlement_delete'),
]
