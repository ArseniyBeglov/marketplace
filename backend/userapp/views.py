import datetime

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
from passlib.hash import sha256_crypt
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from dotenv import load_dotenv
import os

load_dotenv()


@authentication_classes([])
@permission_classes([AllowAny])
class MyUserRegistrationView(APIView):
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # нужно понять как обращаться к данным из сериальзатора, чтобы сразу засовывать туда хэшированный токен
            # а то через такой костыль не хорошо работать
            user = get_user_model().objects.get(email=serializer.data['email'])
            ts = str(datetime.datetime.now().timestamp())
            user.confirm_token = sha256_crypt.hash(ts)
            user.save()


            # и тут скорее всего лучше через id а не email
            uemail = urlsafe_base64_encode(str(user.email).encode('utf-8'))
            activation_url = reverse_lazy('confirm_email', kwargs={'uemail64': uemail, 'token': ts})
            current_site = str(request.get_host())
            send_mail(
                'Confirm email',
                f'http://{current_site}{activation_url}',
                os.environ.get('EMAIL_HOST_USER'),
                [str(serializer.data['email'])],
                fail_silently=False,
            )

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


@authentication_classes([])
@permission_classes([AllowAny])
class MyUserEmailConfirmView(APIView):
    def get(self, request, uemail64, token):
        try:
            uemail = urlsafe_base64_decode(uemail64).decode()
            user = get_user_model().objects.filter(email=uemail).first()
        except (TypeError, ValueError, OverflowError):
            user = None
        if user is not None and sha256_crypt.verify(token, user.confirm_token):
            user.is_confirmed = True
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


