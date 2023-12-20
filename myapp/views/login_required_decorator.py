from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.conf import settings
from myapp.models.user import CustomUser
import jwt


def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Retrieve the 'access_token' cookie from the request
        access_token = request.COOKIES.get('access_token')


        if not access_token:
            return redirect("login")
        try:

            token_payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])


            # Extract information from the payload
            user_id = token_payload['user_id']
            email = token_payload['email']
            user = CustomUser.objects.filter(email=email, id=user_id).first()
            if not user:
                return redirect("login")

            request.user = user

        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden("Access token has expired.")

        except jwt.InvalidTokenError:
            return HttpResponseForbidden("Invalid access token.")

        # Call the original view function
        return view_func(request, *args, **kwargs)

    return _wrapped_view
