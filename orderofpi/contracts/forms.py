from datetimewidget.widgets import DateTimeWidget
from django.forms import DateInput, ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Contract


# Contract form
class ContractForm(ModelForm):

    class Meta:
        model = Contract
        fields = ['issuer', 'target', 'charges', 'indicated_value', 'extend_id', 'trial_date', 'trial_location']

        labels = {
            'indicated_value': _("Donation amount"),
            'extend_id': _('Extend identifier'),
        }

        widgets = {
            # TODO: Need to get this widget to work
            'trial_date': DateTimeWidget(attrs={'id':"div_id_trial_date"}, usel10n = False, bootstrap_version=3),
        }

        help_texts = {
            'extend_id': _('If you want other people to add to this charge, use a unique extension ID.'),
            'charges': _('All charges must be both appropriate and amusing for Justice to be properly served: Running gags, pet peeves, or embarrassing incidents are all good sources of ideas for the charge you make against the Defendant. Be creative and use good taste, for the Justice of Pi is meant to be sweet!'),
        }

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        self.fields['indicated_value'].widget.attrs['placeholder'] = '$20.00'
        self.fields['extend_id'].widget.attrs['placeholder'] = 'ex. bringbobtojustice'