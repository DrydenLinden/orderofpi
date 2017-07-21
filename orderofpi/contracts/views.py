from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .forms import ContractForm, ContractLookUp
from .models import Contract


# Create contract view
def create_contract(request):
    template = "contracts/create_contract.html"

    contract_form = ContractForm(request.POST or None)

    if contract_form.is_valid():
        contract = contract_form.save()

        # TODO: Need to send out an email out here

        return HttpResponseRedirect(reverse('payments:online_payment', kwargs={'contract_id': contract.id}))

    context = {
        'contract_form': contract_form,
    }

    return render(request, template, context)


# Extend contract (Add money to existing contract)
def contract_lookup(request):
    template = "contracts/contract_lookup.html"

    contract_form = ContractLookUp(request.POST or None)

    if contract_form.is_valid():
        extend_id = contract_form.cleaned_data['extend_id']
        contract = Contract.objects.get(extend_id=extend_id)

        return redirect(reverse())

    context = {}
    return render(request, template, context)


# Extend contract (Add money to existing contract)
def extend_contract(request, contract_id):
    template = "contracts/extend_contract.html"



    context = {}
    return render(request, template, context)