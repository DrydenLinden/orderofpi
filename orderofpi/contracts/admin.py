from django.contrib import admin

from .models import Contract, ContractNotes

class ContractNotesInline(admin.TabularInline):
    model = ContractNotes
    extra = 1
    fields = ['contract', 'author', 'text']


class ContractAdmin(admin.ModelAdmin):
    inlines = [ContractNotesInline]


admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractNotes)
