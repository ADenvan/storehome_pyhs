# Редактируем движок базы данных Django.

1. Установка движка базы данных.
2. Изменение атрибутов
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'home',
        "USER": 'home',
        "PASSWORD": 'home',
        "HOST": 'localhost',
        "PORT": '5432',  # Порт по умолчанию для PostgreSQL
    }
}
```

# Установка psycopg2.
```bash
pip install psycopg2
```
