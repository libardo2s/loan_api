from rest_framework import serializers
from apps.customers.models import Customers  # Make sure this import path matches your project structure

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_score(self, value):
        if value is not None and (value < 0 or value > 10000):
            raise serializers.ValidationError("Score must be between 0 and 10000")
        return value