from django.urls import path
from accounts.views import register,user_login,user_logout
from main import views
urlpatterns = [
    path('login', user_login ,name="login"),
    path('register', register ,name="register"),
    path('login', user_logout,name="logout"),
    path('',views.home,name="homepage"),
    path('category/list', views.expense_category_list, name='expense_category_list'),
    path('category/create/', views.expense_category_create, name='expense_category_create'),
    path('category/update/<int:pk>/', views.expense_category_update, name='expense_category_update'),
    path('category/delete/<int:pk>/', views.expense_category_delete, name='expense_category_delete'),
]
