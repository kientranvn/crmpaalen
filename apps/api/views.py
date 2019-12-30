from django.http import JsonResponse

from django.shortcuts import render


# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *agrs, **kwargs):
        data = {
            'name': 'Kien',
            'age': 25
        }    
        return Response(data)

#def test_view(request):
#    data = {
#        'name': 'Kien',
#        'age': 25
#    }    
#    return JsonResponse(data)
