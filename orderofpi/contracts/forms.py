from django.forms import ModelForm
from .models import Contract


# Contract form
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['issuer', 'target', 'charges', 'indicated_value', 'extend_id', 'trial_date', 'trial_location']