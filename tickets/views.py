from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,response
# Create your views here.
def nomodelnorest(request):
    guests=[
        {"name":"amr","mobile":"0123456789"},
        {"name":"ali","mobile":"0987654321"},
    ]
    return JsonResponse(guests,safe=False)
