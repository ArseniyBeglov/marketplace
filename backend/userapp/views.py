from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import MyUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model



@authentication_classes([])
@permission_classes([AllowAny])
class MyUserRegistrationView(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Создайте JWT-токен
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# viewset для put и get запросов
class MyUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put']

    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow unauthenticated access for GET requests
            return []
        return super().get_permissions()