def is_user_admin(request):
    return request.user.is_admin