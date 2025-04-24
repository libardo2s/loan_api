from django.db import models
from django.utils import timezone
from customers.models import CustomersCustomer

class Loans(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.SmallIntegerField()
    contract_version = models.CharField(max_length=30, blank=True, null=True)
    maximum_payment_date = models.DateTimeField(blank=True, null=True)
    taken_at = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(CustomersCustomer, on_delete=models.CASCADE, related_name='loans')
    outstanding = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Loan {self.id} - Amount: {self.amount} - Status: {self.status}"

    class Meta:
        db_table = 'loans_loan'