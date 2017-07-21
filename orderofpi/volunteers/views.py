from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import VolunteerForm



# Assign volunteer view
def assign(request):
    pass
    # template = "volunteers/assign.html"
    # context = {}
    # return render(request, template, context)


# Assign volunteer view
def sign_up(request):
    pass
    # template = "volunteers/sign_up.html"
    #
    # volunteer_form = VolunteerForm(request.POST or None)
    #
    # if volunteer_form.is_valid():
    #     volunteer_form.save()
    #
    #     # TODO: Need to send out an email out here
    #     # TODO: Need to associate available times
    #
    #     return HttpResponseRedirect(reverse('volunteer_joined'))
    #
    # context = {
    #     'volunteer_form': volunteer_form,
    # }
    #
    # return render(request, template, context)


# Assign volunteer view
def view_schedule(request):
    pass
    # template = "volunteers/view_schedule.html"
    # context = {}
    # return render(request, template, context)