from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods' # Имя приложения
    verbose_name = 'Товары' # Название приложения в админке /

