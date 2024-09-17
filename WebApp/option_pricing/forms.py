from django import forms
from .models import Option

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_type', 'underlying_price', 'strike_price', 'volatility', 'time_to_maturity', 'risk_free_rate']
