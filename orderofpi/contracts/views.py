from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import ContractForm


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

    context = {}
    return render(request, template, context)


# Extend contract (Add money to existing contract)
def extend_contract(request, contract_id):
    template = "contracts/extend_contract.html"



    context = {}
    return render(request, template, context)