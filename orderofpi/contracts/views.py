from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404

from .forms import ContractForm, ContractLookUpForm
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

    contract_form = ContractLookUpForm(request.POST or None)

    if contract_form.is_valid():
        extend_id = contract_form.cleaned_data['extend_id']

        try:
            contract = Contract.objects.get(extend_id=extend_id)
            return redirect("payments:extend_contract", contract_id=contract.id)
        except Contract.DoesNotExist:
            messages.error(request, "Sorry, we couldn't find '" + extend_id + "' ¯\_(ツ)_/¯")
            return redirect(reverse("contract_lookup"))


        # return redirect(reverse())

    context = {
        "form": contract_form,
    }
    return render(request, template, context)
