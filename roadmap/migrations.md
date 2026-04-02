
-------------------------------------------
# Управление миграциями Django ORM
```bash
.\manage.py makemigrations   # Создает файлы миграции
.\manage.py migrate          # Применяет миграции к базе данных
.\manage.py createsuperuser  # Создаем суперпользователя
```
-------------------------------------------

1. Создание фаила миграции. Для проверки изменения в модели
    - .\manage.py makemigrations
    - goods\migrations\0002_alter_products_options.py

2. Применение миграций. И создание в таблицы в БД
    - .\manage.py migrate

3. Создание суперпользователя.
    - .\manage.py createsuperuser
    - Username: root
    - Email: -
    - Password: root
