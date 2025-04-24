from django.db import models
from django.utils import timezone
from loans.models import LoansLoan
from customers.models import CustomersCustomer

class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.SmallIntegerField()
    paid_at = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(CustomersCustomer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment {self.id} - Amount: {self.total_amount} - Status: {self.status}"

    class Meta:
        db_table = 'payments_payment'

class Paymentdetail(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    loan = models.ForeignKey(LoansLoan, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)

    def __str__(self):
        return f"PaymentDetail {self.id} - Amount: {self.amount} - Loan: {self.loan.id} - Payment: {self.payment.id}"

    class Meta:
        db_table = 'payments_paymentdetail'
