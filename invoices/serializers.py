from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source="created_by.username")
    total = serializers.ReadOnlyField()

    class Meta:
        model = Invoice
        fields = ["id", "customer", "product", "quantity", "price", "total", "created_by", "created_at"]
        read_only_fields = ["id", "total", "created_by", "created_at"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value
