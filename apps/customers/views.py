# apps/customers/views.py
from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.customers.models import Customers
from apps.customers.serializer import CustomerSerializer
from apps.customers.service import CustomerService


class CustomerAPIView(APIView):
    def post(self, request):
        """Create a new customer with active status"""
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                customer = CustomerService.create_customer(
                    external_id=serializer.validated_data["external_id"],
                    score=serializer.validated_data.get("score"),
                    pre_approved_at=serializer.validated_data.get("pre_approved_at"),
                )
                return Response(
                    {
                        "external_id": customer.external_id,
                        "status": customer.status,
                        "score": float(customer.score) if customer.score else None,
                        "preapproved_at": (
                            customer.pre_approved_at.isoformat()
                            if customer.pre_approved_at
                            else None
                        ),
                    },
                    status=status.HTTP_201_CREATED,
                )
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, customer_id=None):
        """Get customer(s)"""
        if customer_id:
            try:
                customer = CustomerService.get_customer_by_id(customer_id)
                return Response(CustomerSerializer(customer).data)
            except Customers.DoesNotExist:
                return Response(
                    {"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND
                )
        else:
            customers = CustomerService.get_all_active_customers()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
