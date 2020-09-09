from django.urls import path
from .views import DashboardView, check_link
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'teachers'
urlpatterns = [
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', LoginView.as_view(), name="login_page"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('sync/', check_link, name="sync"),
]
