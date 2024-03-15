from django.urls import path
from accounts.views import register,user_login,user_logout
from main.views import home,expensecategory_views
urlpatterns = [
    path('login', user_login ,name="login"),
    path('register', register ,name="register"),
    path('login', user_logout,name="logout"),
    path('',home,name="homepage"),
    path('expense_cateory',expensecategory_views,name="expense_category_views")
]
