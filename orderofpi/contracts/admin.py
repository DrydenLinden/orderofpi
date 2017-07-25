from django.contrib import admin
from django.shortcuts import render

from .models import Contract, ContractNotes

def print_contract(modeladmin, request, queryset):

    template = "contracts/print_contract.html"

    if queryset.count() != 1:
        modeladmin.message_user(request, "Can not print more than one contract at a time.")
        return

    for item in queryset:
        contract = item

    context = {
        'contract_info': contract,
    }

    return render(request, template, context)

print_contract.short_description = "Print contract for the trial."

class ContractNotesInline(admin.TabularInline):
    model = ContractNotes
    extra = 1
    fields = ['contract', 'author', 'text']


class ContractAdmin(admin.ModelAdmin):
    inlines = [ContractNotesInline]
    actions = [print_contract]


admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractNotes)
