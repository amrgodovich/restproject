from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# use package-relative imports so Python finds the app modules
from .serializers import GuestSerializer, MovieSerializer, ReservationSerlaizer
from .models import Guest, Reservation, Movie
from rest_framework.views import APIView
# Create your views here.
def nomodelnorest(request):
    guests=[
        {"name":"amr","mobile":"0123456789"},
        {"name":"ali","mobile":"0987654321"},
    ]
    return JsonResponse(guests,safe=False)

@api_view(['GET','POST'])
def FBV_List(request):
    if request.method=='GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def FBV_PK(request,pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    if request.method=='PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CBV_List(APIView):
    def get(self,request):
        guests=Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GuestSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
