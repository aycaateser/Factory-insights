from datetime import timedelta
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render
import jwt
from myapp.models.user import CustomUser
from django.conf import settings


def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = CustomUser.objects.filter(email=email).first()

        if not user:
            return render(request, 'login.html', {'error_message': 'Kullanıcı bulunamadı'})

        if not user.check_password(password):
            return render(request, 'login.html', {'error_message': 'Şifreniz hatalı'})

        # Token süresi ve içeriği
        token_payload = {
            'user_id': user.id,
            'email': user.email,
            'is_admin': user.is_admin,
            'exp': datetime.utcnow() + timedelta(days=1),  # Token süresi (örnekte 1 gün)
        }

        # Token oluşturma
        token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
        # Set the 'access_token' cookie in the response
        response = redirect('home')
        response.set_cookie('access_token', token)

        return response

    return render(request, 'login.html')
