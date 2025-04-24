# apps/customers/services.py
from django.core.exceptions import ValidationError
from .models import Customers

class CustomerService:
    ACTIVE_STATUS = 1
    
    @classmethod
    def create_customer(cls, external_id, score=None, pre_approved_at=None):
        """
        Creates a new customer with active status
        Args:
            external_id: External identifier for the customer
            score: Credit score (optional)
            pre_approved_at: Pre-approval datetime (optional)
        Returns:
            The created Customer instance
        """
        customer = Customers(
            external_id=external_id,
            status=cls.ACTIVE_STATUS,
            score=score,
            pre_approved_at=pre_approved_at
        )
        
        customer.full_clean()  # Validate model fields
        customer.save()
        return customer
    
    @classmethod
    def get_customer_by_id(cls, customer_id):
        """
        Retrieves a customer by primary key
        Args:
            customer_id: Customer ID
        Returns:
            Customer instance
        Raises:
            Customers.DoesNotExist: If customer not found
        """
        return Customers.objects.get(id=customer_id)
    
    @classmethod
    def get_customer_by_external_id(cls, external_id):
        """
        Retrieves a customer by external ID
        Args:
            external_id: External identifier
        Returns:
            Customer instance or None if not found
        """
        try:
            return Customers.objects.get(external_id=external_id)
        except Customers.DoesNotExist:
            return None
    
    @classmethod
    def get_all_active_customers(cls):
        """
        Retrieves all active customers
        Returns:
            QuerySet of active customers
        """
        return Customers.objects