from django.db import models


# Transaction model
class Transaction(models.Model):
    contract = models.ForeignKey('contracts.Contract', on_delete=models.PROTECT)

    # Transaction basic details
    TYPE_CHOICES = (
        ('online_cc', 'Online Credit Card'),
        ('offline_cc', 'In Office Credit Card'),
        ('cash', 'Cash'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    # Stripe attributes, can be empty due to cash transaction
    stripe_status = models.CharField(max_length=50, null=True)
    stripe_id = models.CharField(max_length=20, null=True)
