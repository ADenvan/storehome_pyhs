# Создание фикстуры для перехода на Postgres SQL
https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes

```bash
python manage.py loaddata    # Загружает фикстуры в базу данных
python manage.py dumpdata    # Экспортирует данные в JSON файл
```

1. Создаем папку `fixtures/goods/`
2. Командой в терминале создаем фаил `cats.json` и заполняем его данными в формате JSON.
    - Могут быть проблемы с кодировкой.


**Команда создает неверную кодировку**
```bash
.\manage.py dumpdata goods.Categories > fixtures/goods/categories.json
```
1. Django выводит данные в __UTF-8__ (правильная кодировка)
2. PowerShell перехватывает вывод и сохраняет его в __CP866__
3. Результат — кракозябры (mojibake)

### Как избежать проблемы
__Вариант 1:__ Использовать флаг `--output` у dumpdata:

**Нужно Тестировать**
```bash
.\manage.py dumpdata goods.Products --output fixtures/goods/products.json
```
.\manage.py dumpdata goods.Products --output fixtures/goods/prod.json


3. Загружаем данные в базу данных
```bash
.\manage.py loaddata fixtures/goods/cats.json
```