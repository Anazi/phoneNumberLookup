from django.db import models

from v1.phoneNumbers.validators import validate_area_code, validate_country_code, validate_phone_number


class PhoneNumber(models.Model):
    phoneNumber = models.CharField(max_length=15, primary_key=True, validators=[validate_phone_number])
    countryCode: models.CharField = models.CharField(max_length=2, null=True, validators=[validate_country_code])
    areaCode: models.IntegerField = models.IntegerField(validators=[validate_area_code])
    localPhoneNumber: models.IntegerField = models.IntegerField()

    def __str__(self):
        return f'phoneNumber:{self.phoneNumber}, countryCode:{self.countryCode}, areaCode:{self.areaCode}, ' \
               f'localPhoneNumber:{self.localPhoneNumber}'
