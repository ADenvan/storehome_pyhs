from django.urls import path
from goods import views

# Маршрут для страницы каталога товаров.

app_name = 'goods'  # Устанавливаем имя приложения для использования в шаблонах и других местах кода

urlpatterns = [ # Список маршрутов приложения
    path('<slug:category_slug>/', views.catalog, name='index'), # Добавляем маршрут для главной страницы
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    # path('product/', views.product, name='product'), # Добавляем маршрут для страницы "О нас"
    path('product/<slug:product_slug>/', views.product, name='product'), # Добавляем URL-маршрутизацию для страницы.

    # path('product/<int:product_id>/', views.product, name='product'), # Добавляем URL-маршрутизацию для страницы.
]