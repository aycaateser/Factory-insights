from django.shortcuts import render

def logout_view(request):
    del request.COOKIES['access_token']
    return render(request, 'login.html')