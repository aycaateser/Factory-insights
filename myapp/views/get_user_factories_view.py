def get_user_factories(user):
    if not user:
        return None

    user_factories = user.factory_set.filter(is_active=True)

    return user_factories
