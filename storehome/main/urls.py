from django.urls import path
from main import views

app_name = 'main'  # Устанавливаем имя приложения для использования в шаблонах и других местах кода


urlpatterns = [ # Список маршрутов приложения
    path('', views.index, name='index'), # Добавляем маршрут для главной страницы
    path('about/', views.about, name='about'), # Добавляем маршрут для страницы "О нас"
]