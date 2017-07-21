from django.shortcuts import render, get_object_or_404, reverse
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from contracts.models import Contract
from .models import Transaction
from datetime import datetime
import stripe


# Create your views here.
def online_payment(request, contract_id):
    template = "payments/online_payment.html"

    contract = get_object_or_404(Contract , id=contract_id)

    context = {
        'contract':contract,
        'indicated_value': contract.indicated_value * 100,
        'stripe_key': settings.STRIPE_TEST_API_KEY,
        'contract_id':contract.id
    }
    return render(request, template, context)

def checkout(request):

    contract = get_object_or_404(Contract, id=request.POST['contract_id'])
    stripe.api_key = settings.STRIPE_TEST_SECRET_API_KEY
    token = request.POST['stripeToken']

    try:
        charge = stripe.Charge.create(
            amount=int(contract.indicated_value * 100),
            currency="cad",
            source=token,  # obtained with Stripe.js
            description="Donation",
            receipt_email=request.POST['stripeEmail']
        )

    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught
        template = "payments/online_payment.html"
        messages.error(request,'Stripe Card Error.')
        return render(request, template, context=request.POST)

    except stripe.error.RateLimitError as e:

        template = "payments/online_payment.html"
        messages.error(request, 'Stripe request error.')
        return render(request, template, context=request.POST)

    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        template = "payments/online_payment.html"
        messages.error(request, 'Invalid information')
        return render(request, template, context=request.POST)

    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        template = "payments/online_payment.html"
        messages.error(request, 'Something went wrong.')
        return render(request, template, context=request.POST)

    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        template = "payments/online_payment.html"
        messages.error(request, 'Couldn\'t connect to stripe')
        return render(request, template, context=request.POST)

    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        template = "payments/online_payment.html"
        messages.error(request, 'Something went wrong.')
        return render(request, template, context=request.POST)

    except Exception as e:
        # Something else happened, completely unrelated to Stripe
        template = "payments/online_payment.html"
        messages.error(request, 'Something went wrong.')
        return render(request, template, context=request.POST)

    payment = Transaction(
        contract=contract,
        type='online_cc',
        amount=contract.indicated_value,
        email=request.POST['stripeEmail'],
        stripe_id=charge['id'],
        status=charge['status'],
        date=datetime.now()
    )
    payment.save()

    messages.success(request, 'Payment Successful, Thank you!')
    return HttpResponseRedirect(reverse('sent_contract'))


def pay_later(request):
    template = "payments/pay_later.html"

    return render(request, template)