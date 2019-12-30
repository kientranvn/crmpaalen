// This lib will be export the json format
from django.http import JsonResponse

from django.shortcuts import render



def test_view(request):
    data = {
        'name': 'Kien',
        'age': 25
    }
    
    return JsonResponse(data)
