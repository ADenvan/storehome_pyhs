from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Контроллер главной страницы.
# Здесь можно добавить логику для обработки запроса на главную страницу.
def index(request):

    context = { # Контекст для передачи данных в шаблон.
        'page_title': 'Home', # Заголовок страницы.
        'page_content': 'Welcome to our website!', # Содержимое страницы.
        'footer_content': 'Примеры использования шаблонизатора.', # Содержимое футера.

        'footer_links': [
            {'name': 'Privacy Policy', 'url': '/privacy-policy/'}, # Ссылки в футере.
            {'name': 'Terms of Service', 'url': '/terms-of-service/'} # Ссылки в футере.
        ], # Ссылки в футере.
        'is_authenticated': True, # Флаг аутентификации пользователя.
        'user': [None, 1, "string"], # Объект пользователя.


    }
    return render(request, 'main/index.html', context) # Возвращаем шаблон главной страницы в ответ на запрос.

