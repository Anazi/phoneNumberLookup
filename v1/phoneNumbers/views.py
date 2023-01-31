from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request

from v1.phoneNumbers.service import PhoneNumberService


@api_view(['GET', 'POST', 'DELETE'])
def views_index(request: Request):
    try:
        phone_number_service: PhoneNumberService = PhoneNumberService()
        if request.method == 'GET':
            query = request.GET.get('phoneNumber')
            if query is not None:
                return phone_number_service.get_by_phone_number(request=request, pk=query)
            return phone_number_service.get_all_phone_numbers()

        if request.method == 'POST':
            return phone_number_service.add_phone_number(request=request)

        if request.method == 'DELETE':
            return phone_number_service.delete_all_records()

    except Exception as e:
        response = JsonResponse({
            'request': request.data,
            'error': e.args[0]
        })
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response
