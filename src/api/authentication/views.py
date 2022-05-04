import datetime
from rest_framework import generics, permissions, response, status, views
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    LogoutSerializer
)
from django.contrib.auth import logout
from src.api.users.renderers import UserJSONRenderer
from src.api.users.models import User
from src.api.users.serializers import UserSerializer

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('welcome')

class LogoutAPIView(generics.GenericAPIView):
    """
    Logs out a user on the server.
    - Send the refresh token in the request body as refresh_token
    """
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"is_logged_in": False}, status=status.HTTP_200_OK)

class RegistrationAPIView(generics.GenericAPIView):

    permission_classes = (permissions.AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot  as we go
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
       
        return response.Response(user_data, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):

    """
    Logs in a user,
    creates an access token and a refresh token
    access token is short lived, refresh it using the refresh token endpoint
    """

    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        res = response.Response(serializer.data, status=status.HTTP_200_OK)

        refresh_token_max_age = 86400

        refresh_token_expires = datetime.datetime.utcnow(
        ) + datetime.timedelta(seconds=refresh_token_max_age)

        res.set_cookie(
            key='refresh',
            value=serializer.data.get('tokens').get('refresh'),
            httponly=True,
            expires=refresh_token_expires.strftime(
                "%a, %d-%b-%Y %H:%M:%S UTC"),
            max_age=refresh_token_max_age,
            domain="127.0.0.1:3000"
        )

        return res

class AuthUserAPIView(generics.GenericAPIView):
    """
    Retrieves the logged in user information
    """
    serializer_class = UserSerializer
    pagination_class = None
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        if not request.user:
            return response.Response({'is_logged_in': False}, status=status.HTTP_200_OK)

        data = User.objects.get(email=request.user['email'])
        serializer = self.serializer_class(data)
        response_data = serializer.data
        response_data['is_logged_in'] = True
        return response.Response(response_data, status=status.HTTP_200_OK)