from django.test import TestCase

from rest_framework.exceptions import APIException

from v1.phoneNumbers.validators import validate_area_code, validate_country_code, validate_local_phone_no_by_phone_no, \
    validate_phone_number, validate_phone_number_with_country_code


class TestStringMethods(TestCase):

    def test_validate_area_code(self):
        dummy_valid_area_code_1 = 123
        dummy_valid_area_code_2 = 1234

        dummy_invalid_area_code_1 = 1
        dummy_invalid_area_code_2 = 12
        dummy_invalid_area_code_3 = 12345

        self.assertEqual(
            first=validate_area_code(areaCode=dummy_valid_area_code_1),
            second=None,
            msg='[Positive Test - Area Code 1] Is with 3-4 Digits.'
        )
        self.assertEqual(
            first=validate_area_code(areaCode=dummy_valid_area_code_2),
            second=None,
            msg='[Positive Test - Area Code 2] Is with 3-4 Digits.'
        )

        with self.assertRaises(Exception, msg='[Negative Test - Area Code 1] NOT within 3-4 Digits.'):
            validate_area_code(areaCode=dummy_invalid_area_code_1)
        with self.assertRaises(Exception, msg='[Negative Test - Area Code 2] NOT within 3-4 Digits.'):
            validate_area_code(areaCode=dummy_invalid_area_code_2)
        with self.assertRaises(Exception, msg='[Negative Test - Area Code 3] NOT within 3-4 Digits.'):
            validate_area_code(areaCode=dummy_invalid_area_code_3)

    def test_validate_country_code(self):
        valid_country_code_1 = 'CA'
        valid_country_code_2 = 'CA'

        invalid_country_code_1 = 'XX'
        invalid_country_code_2 = 'xx'

        self.assertEqual(
            first=validate_country_code(country_code=valid_country_code_1),
            second=None,
            msg='[Positive Test - Country Code 1] Is valid as per ISO 3166-1 alpha-2 format.'
        )
        self.assertEqual(
            first=validate_country_code(country_code=valid_country_code_2),
            second=None,
            msg='[Positive Test - Country Code 2] Is valid as per ISO 3166-1 alpha-2 format.'
        )

        with self.assertRaises(Exception,
                               msg='[Negative Test - Country Code 1] Is INVALID as per ISO 3166-1 alpha-2 format.'):
            validate_country_code(country_code=invalid_country_code_1)
        with self.assertRaises(Exception,
                               msg='[Negative Test - Country Code 2] Is INVALID as per ISO 3166-1 alpha-2 format.'):
            validate_country_code(country_code=invalid_country_code_2)

    def test_validate_phone_number(self):
        valid_phone_numbers_1 = '+12125690123'
        valid_phone_numbers_2 = '+52 631 3118150'
        valid_phone_numbers_3 = '34 915 872200'
        valid_phone_numbers_4 = '915 872200'
        valid_phone_numbers_5 = '34915872200'
        valid_phone_numbers_6 = '34 915872200'

        invalid_phone_numbers_1 = '351 21 094 2000'
        invalid_phone_numbers_2 = '+52631 3118150'
        invalid_phone_numbers_3 = '+52 631 31181501'

        self.assertEqual(
            first=validate_phone_number(phone_number=valid_phone_numbers_1),
            second=None,
            msg='[Positive Test - Phone Number 1] Is in E.164 format: [+][country code][area code][local phone number] '
                'and/or acceptable format'
        )
        self.assertEqual(
            first=validate_phone_number(phone_number=valid_phone_numbers_2),
            second=None,
            msg='[Positive Test - Phone Number 2] Is in E.164 format: [+][country code][area code][local phone number] '
                'and/or acceptable format'
        )
        self.assertEqual(
            first=validate_phone_number(phone_number=valid_phone_numbers_3),
            second=None,
            msg='[Positive Test - Phone Number 3] Is in E.164 format: [+][country code][area code][local phone number] '
                'and/or acceptable format'
        )
        self.assertEqual(
            first=validate_phone_number(phone_number=valid_phone_numbers_4),
            second=None,
            msg='[Positive Test - Phone Number 4] Is in E.164 format: [+][country code][area code][local phone number] '
                'and/or acceptable format'
        )
        self.assertEqual(
            first=validate_phone_number(phone_number=valid_phone_numbers_5),
            second=None,
            msg='[Positive Test - Phone Number 5] Is in E.164 format: [+][country code][area code][local phone number] '
                'and/or acceptable format'
        )
        self.assertEqual(
            first=validate_phone_number(phone_number=valid_phone_numbers_6),
            second=None,
            msg='[Positive Test - Phone Number 6] Is in E.164 format: [+][country code][area code][local phone number] '
                'and/or acceptable format'
        )

        with self.assertRaises(Exception,
                               msg='[Negative Test - Phone No. 1] Is NOT in E.164 format: [+][country code][area code]'
                                   '[local phone number] and/or acceptable format'):
            validate_phone_number(phone_number=invalid_phone_numbers_1)
        with self.assertRaises(Exception,
                               msg='[Negative Test - Phone No. 2] Is NOT in E.164 format: [+][country code][area code]'
                                   '[local phone number] and/or acceptable format'):
            validate_phone_number(phone_number=invalid_phone_numbers_2)
        with self.assertRaises(Exception,
                               msg='[Negative Test - Phone No. 3] Is NOT in E.164 format: [+][country code][area code]'
                                   '[local phone number] and/or acceptable format'):
            validate_phone_number(phone_number=invalid_phone_numbers_3)

    def test_validate_phone_number_with_country_code(self):
        dummy_phone_number_with_cc = '+52 631 3118159'
        dummy_phone_number_no_cc = '631 3118159'

        dummy_no_cc = None
        dummy_cc = 'XX'

        self.assertEqual(
            first=validate_phone_number_with_country_code(phone_number=dummy_phone_number_with_cc,
                                                          country_code=dummy_cc),
            second=None,
            msg='[Positive Test - Phone No. with Country Code 1] Field "country_code" does not matter.'
        )
        self.assertEqual(
            first=validate_phone_number_with_country_code(phone_number=dummy_phone_number_with_cc,
                                                          country_code=dummy_no_cc),
            second=None,
            msg='[Positive Test - Phone No. with Country Code 2] Field "country_code" does not matter.'
        )

        with self.assertRaises(APIException, msg='[Negative Test - Phone No. with Country Code 1] Phone no. with no '
                                                 'country code and Field - country code "null"'):
            validate_phone_number_with_country_code(phone_number=dummy_phone_number_no_cc, country_code=dummy_no_cc)

    def test_validate_local_phone_number(self):
        phone_no_1 = '+12125690123'
        phone_no_2 = '+121256901235'

        valid_local_phone_no_1 = 690123
        valid_local_phone_no_2 = 6901235

        invalid_local_phone_no_1 = 12345
        invalid_local_phone_no_2 = 12345678

        self.assertEqual(
            first=validate_local_phone_no_by_phone_no(phone_number=phone_no_1, local_phone_number=valid_local_phone_no_1),
            second=None,
            msg='[Positive Test - Phone no Vs Local Phone No 1] phoneNumber and localPhoneNumber are the same.'
        )
        self.assertEqual(
            first=validate_local_phone_no_by_phone_no(phone_number=phone_no_2, local_phone_number=valid_local_phone_no_2),
            second=None,
            msg='[Positive Test - Phone no Vs Local Phone No 1] phoneNumber and localPhoneNumber are the same.'
        )

        with self.assertRaises(Exception,
                               msg='[Negative Test - Phone no Vs Local Phone No 1] phoneNumber and localPhoneNumber are the same.'):
            validate_local_phone_no_by_phone_no(phone_number=phone_no_1, local_phone_number=invalid_local_phone_no_1)
        with self.assertRaises(Exception,
                               msg='[Negative Test - Phone no Vs Local Phone No 1] phoneNumber and localPhoneNumber are the same.'):
            validate_local_phone_no_by_phone_no(phone_number=phone_no_2, local_phone_number=invalid_local_phone_no_2)


# if __name__ == '__main__':
#     unittest.main()
