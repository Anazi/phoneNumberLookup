from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from v1.phoneNumbers.models import PhoneNumber
from v1.phoneNumbers.serializers import PhoneNumberSerializer
from v1.phoneNumbers.validators import validate_phone_number_with_country_code, validate_local_phone_no_by_phone_no


class PhoneNumberService:
    @staticmethod
    def get_all_phone_numbers():
        try:
            phone_number = PhoneNumber.objects.all()
            serializer = PhoneNumberSerializer(phone_number, many=True)
            return JsonResponse({'phone-numbers': serializer.data})
        except Exception as e:
            err = {
                'error': {
                    'phoneNumber': e.args[0]
                }
            }
            response = JsonResponse(err)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response

    @staticmethod
    def get_by_phone_number(request: Request, pk):
        try:
            phone_number = PhoneNumber.objects.get(pk=pk)
        except Exception as e:
            err = {
                'phoneNumber': request.GET.get('phoneNumber'),
                'error': {
                    'phoneNumber': f'{e.args[0]} INVALID value and/or NOT ENCODED properly.'
                }
            }
            response = JsonResponse(err)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response

        serializer = PhoneNumberSerializer(phone_number)
        return Response(serializer.data)

    @staticmethod
    def add_phone_number(request: Request):
        try:
            serializer: PhoneNumberSerializer = PhoneNumberSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                phone_number = serializer.validated_data.get('phoneNumber')

                country_code = serializer.validated_data.get('countryCode')
                validate_phone_number_with_country_code(phone_number=phone_number, country_code=country_code)

                local_phone_number = serializer.validated_data.get('localPhoneNumber')
                validate_local_phone_no_by_phone_no(phone_number=phone_number, local_phone_number=local_phone_number)

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            msg = {
                'phoneNumber': request.data.get('phoneNumber'),
                'error': e.args[0]
            }
            response = JsonResponse(msg)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response

    @staticmethod
    def delete_all_records():
        try:
            PhoneNumber.objects.all().delete()
            return JsonResponse(data={}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            err = {
                'error': e.args[0]
            }
            response = JsonResponse(err)
            response.status_code = status.HTTP_400_BAD_REQUEST
            return response
