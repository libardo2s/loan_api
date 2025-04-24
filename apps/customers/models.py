from django.db import models
from django.utils import timezone

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=60, blank=True, null=True, unique=True)
    status = models.SmallIntegerField(blank=True, null=True, default=1)
    score = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    pre_approved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Customer {self.id} - Status: {self.status}"

    class Meta:
        db_table = 'customers_customer'
