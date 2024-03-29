import jwt
from .models import Jwt
from user.models import CustomUser
from datetime import datetime,timedelta
from django.conf import settings
import random
import string
from rest_framework.views import APIView
from .serializers import LoginSerializer,RegisterSerialzer,RefreshSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .authentication import Authenttication

def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase+string.digits,k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp":datetime.now()+timedelta(minutes=5),**payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

def get_refresh_token():
    return jwt.encode(
        {"exp":datetime.now()+timedelta(days=365),"data":get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data['email'],password=serializer.validated_data['password'])

        if not user:
            return Response({"error":"Invalid email or password"},status=400)

        Jwt.objects.filter(user_id=user.id).delete()    

        access = get_access_token({"user_id":user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id,access=access.decode(),refresh=refresh.decode()
        )

        return Response({"access":access,"refresh":refresh})

class RegisterView(APIView):
    serializer_class = RegisterSerialzer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
         
        CustomUser.objects._create_user(**serializer.validated_data)

        return Response({"success":"User created Successfully"})




class RefreshView(APIView):
    serializer_class = RefreshSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            active_jwt = Jwt.objects.get(
                refresh = serializer.validated_data["refresh"]
            )
        except Jwt.DoesNotExist:
            return Response({"error":"refresh token not found"},status=400)

        if not Authenttication.verify_token(serializer.validated_data["refresh"]):
            return Response({"error":"Token is invalid or has expired"})

        access = get_access_token({"user_id":active_jwt.user.id})
        refresh = get_refresh_token()

        active_jwt.access = access.decode()
        active_jwt.refresh = refresh.decode()

        return Response({"access":access,"refresh":refresh})


def validate_request(headers):
    authorization = headers.get("Authorization",None)
    if not authorization:
        raise Exception("You need to provide authorization token")

    token = headers["Authorization"][7:]
    decoded_data = Authenttication.verify_token(token)

    if not decoded_data:
        raise Exception("Token is not valid or expired")

    return decoded_data

class GetSecureInfo(APIView):

    def get(self,request):
        validate_request(request.headers)

        return Response({"data":"This is a secured info"})



