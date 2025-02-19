from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
# Create your views here.
from django.http import HttpResponse
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking
from django.contrib.auth.models import User


def sayHello(request):
    return HttpResponse('Hello World')



# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]