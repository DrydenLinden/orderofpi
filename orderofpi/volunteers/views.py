from django.shortcuts import render

# Volunteer views

# Assign volunteer view
def assign(request):
    template = "volunteers/assign.html"
    context = {}
    return render(request, template, context)


# Assign volunteer view
def sign_up(request):
    template = "volunteers/sign_up.html"
    context = {}
    return render(request, template, context)


# Assign volunteer view
def view_schedule(request):
    template = "volunteers/view_schedule.html"
    context = {}
    return render(request, template, context)