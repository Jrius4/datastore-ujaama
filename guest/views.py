from django.shortcuts import render
from .models import Guest
from rest_framework.response import Response
from .serializers import GuestProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from api.permissions import IsLoggedInUserOrAdmin,IsAdminUser
from rest_framework.views import APIView

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action =='patch':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes= [IsAdminUser]
        return [permission() for permission in permission_classes]
# Protected views
# Need a jwt token header to access this view
class GuestHelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'message':'Hello, guest!'}
        return Response(content)
