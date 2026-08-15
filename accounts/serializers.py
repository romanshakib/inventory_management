from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = ["username", "email", "phone", "address"]

    def validate_phone(self, value):
        if value and len(value) < 7:
            raise serializers.ValidationError("Phone number is too short.")
        return value
