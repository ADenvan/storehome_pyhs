from django.urls import path
from goods import views

app_name = 'goods'  # Устанавливаем имя приложения для использования в шаблонах и других местах кода


urlpatterns = [ # Список маршрутов приложения
    path('', views.catalog, name='index'), # Добавляем маршрут для главной страницы
    path('product/', views.product, name='product'), # Добавляем маршрут для страницы "О нас" 
]