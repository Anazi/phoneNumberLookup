import json

from django.test import TestCase
from v1.phoneNumbers.models import PhoneNumber


class PhoneNumberTest(TestCase):
    # models test
    @staticmethod
    def create_phone_number(phone_number='+52 631 3118150', country_code='US', area_code=123,
                            local_phone_number=3118150):
        return PhoneNumber.objects.create(phoneNumber=phone_number, countryCode=country_code, areaCode=area_code,
                                          localPhoneNumber=local_phone_number)

    def test_phone_number_creation(self):
        ph_no_obj = self.create_phone_number()
        self.assertTrue(isinstance(ph_no_obj, PhoneNumber))

    # views (uses reverse)
    def test_phone_number_view(self):
        test_url = 'http://127.0.0.1:8000/v1/phone-numbers'

        ph_no_obj: PhoneNumber = self.create_phone_number()
        resp = self.client.get(test_url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(ph_no_obj.phoneNumber, json.loads(resp.content).get("phone-numbers")[0].get("phoneNumber"))
