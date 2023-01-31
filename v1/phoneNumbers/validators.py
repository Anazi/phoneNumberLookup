import re

import pycountry
from rest_framework.exceptions import APIException
from django.db.models import IntegerField, CharField


def validate_area_code(areaCode: int):
    if not 2 < len(str(areaCode)) <= 4:
        err = {
                'areaCode': f'{areaCode} - INVALID value. MUST be 3-4 digits ONLY.'
            }
        raise APIException(err)


def validate_country_code(country_code: str):
    if not pycountry.countries.get(alpha_2=country_code) or not str(country_code).isupper():
        err = {
                'country_code': f'{country_code} INVALID.'
                                f' MUST be in ISO 3166-1 alpha-2 format ONLY and/or a valid country code.'
            }
        raise APIException(err)


def validate_phone_number(phone_number):
    phone_number_regex: str = r'^(\+?(\d{1,3}\s)?(\d{3,4}\s?\d{6,7}))$'

    if re.match(pattern=phone_number_regex, string=phone_number) is None:
        err = {
            'phoneNumber': 'phone_number MUST be in E.164 format: [+][country code][area code][local phone number] and/or acceptable format.'
        }
        raise APIException(err)


def validate_phone_number_with_country_code(phone_number, country_code):
    no_country_code_regex: str = r'(\d{9,11})|((\d{3,4}\s?)\d{6,7})'

    if re.match(pattern=no_country_code_regex, string=phone_number) is not None:
        if country_code is None:
            raise APIException({
                "countryCode": "required value is missing"
            })


def validate_local_phone_no_by_phone_no(phone_number, local_phone_number):
    stripped_phone_number: str = str(phone_number).strip()
    last_6: int = int(str(stripped_phone_number)[-6:])
    last_7: int = int(str(stripped_phone_number)[-7:])

    if not ((last_6 == local_phone_number) or (last_7 == local_phone_number)):
        raise APIException({
            "countryCode": "phoneNumber and localPhoneNumber are not the same"
        })
