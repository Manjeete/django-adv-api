import jwt
from datetime import datetime
from django.conf import settings


class Authenttication():


    @staticmethod
    def verify_token(token):
        try:
            decoded_data = jwt.decode(token,settings.SECRET_KEY,algorithm="HS256")
        except Exception:
            return None
        
        # Check if token is expired
        exp = decoded_data["exp"]

        if datetime.now().timestamp() > exp:
            return None 

        return decoded_data 