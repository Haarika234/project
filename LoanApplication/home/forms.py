from django import forms
from home.models import UserProfile, FinancialProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'phone', 'age', 'address']
        
        
class FinancialForm(forms.ModelForm):
    class Meta:
        model = FinancialProfile
        fields = ['monthly_income', 'requested_loan_amount', 'tenure']
        