from django.urls import path
from accounts import views

app_name="accounts"

urlpatterns = [
    path('', views.signup, name="signup"),
    path('login/', views.login_view, name='login'),
]