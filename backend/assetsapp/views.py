from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Asset
from .serializers import AssetSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class AssetPagination(PageNumberPagination):
    page_size = 10  # Установите желаемое количество записей на странице
    page_size_query_param = 'page_size'
    max_page_size = 100

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = AssetPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow unauthenticated access for GET requests
            return []
        return super().get_permissions()