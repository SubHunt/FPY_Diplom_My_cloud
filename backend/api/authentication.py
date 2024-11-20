from tastypie.authentication import ApiKeyAuthentication

# Добавляем свой класс и метод для работы с запросами.
# Для метода GET Аутентификация не нужна, поэтому мы переписываем метод is_authenticated
# Для других методов мы вызываем родительский метод is_authenticated


class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return super().is_authenticated(request, **kwargs)
