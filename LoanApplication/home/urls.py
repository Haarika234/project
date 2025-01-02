from django.urls import path
from home import views

app_name="home"

urlpatterns = [
    path('', views.home, name="home"),
    path("profiles/", views.Profile, name="profile"),
    path("financial/", views.Financial, name="financial")
]