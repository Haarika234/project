from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255)  # Name field with max length
    email = models.EmailField(unique=True)  # Email field with unique constraint
    phone = models.CharField(max_length=15, unique=True)  # Phone field with max length and uniqueness
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)])  # Age field with min and max value validators
    address = models.TextField()  # Address field, using TextField for multi-line address storage

    def __str__(self):
        return self.name
    
    
class FinancialProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='financial_profile')
    monthly_income = models.DecimalField(max_digits=15, decimal_places=2) 
    requested_loan_amount = models.DecimalField(max_digits=15, decimal_places=2)  
    tenure = models.PositiveIntegerField()  # Loan tenure (e.g., number of months) as a positive integer

    def __str__(self):
        return f"{self.user.username}'s Financial Profile"