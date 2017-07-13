from django.db import models


# Contract model. Used for...
class Contract(models.Model):
    target = models.CharField(max_length=30)
    issuer = models.CharField(max_length=30)
    indicated_value = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField(auto_now_add=True)
    charges = models.TextField()

    # If the contract allows funds to be added using an extension id
    extend_id = models.CharField(max_length=60, blank=True)

    # OoP Trial information
    trial_date = models.DateTimeField()
    trial_location = models.CharField(max_length=30)

    def __str__(self):
        return self.issuer + " is charging " + self.target + " $" + str(self.indicated_value) + " on the date of " + str(self.trial_date)


# Contract notes model. Extension of the contract
class ContractNotes(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    text = models.CharField(max_length=200)
