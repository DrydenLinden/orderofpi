from django.contrib import admin

from .models import Contract, ContractNotes

class ContractNotesInline(admin.TabularInline):
    model = ContractNotes
    extra = 1
    fields = ['contract', 'author', 'text']


class ContractAdmin(admin.ModelAdmin):
    inlines = [ContractNotesInline]
    list_display = ['target', 'issuer', 'trial_date', 'trial_location', 'status', 'indicated_value', 'actual_value']
    readonly_fields = ['actual_value']

    def actual_value(self,obj):
        return obj.GetActualDonation()
    
admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractNotes)
