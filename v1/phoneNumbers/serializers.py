from rest_framework import serializers

from v1.phoneNumbers.models import PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['phoneNumber', 'countryCode', 'areaCode', 'localPhoneNumber']
