from django.shortcuts import render

# Contract views


# Create contract view
def create_contract(request):
    template = "contracts/create_contract.html"
    context = {}
    return render(request, template, context)


# Extend contract (Add money to existing contract)
def extend_contract(request):
    template = "contracts/extend_contract.html"
    context = {}
    return render(request, template, context)

