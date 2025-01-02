from django.contrib import admin
from home.models import UserProfile, FinancialProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(FinancialProfile)