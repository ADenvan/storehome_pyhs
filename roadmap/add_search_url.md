# Добавляем URL маршрут в маршрутизатор.
1. Открываем файл `urls.py` в приложении, где нужно добавить маршрут.
2. ВНИМАНИЕ ВАЖНО очередность маршрутов важна, так как Django проверяет маршруты сверху вниз и выбирает первый подходящий маршрут. Поэтому если маршрут поиска будет выше маршрута каталога, то поиск не будет работать.
```python
urlpatterns = [ # Список маршрутов приложения
    path('search/', views.catalog, name='search'),
]
```

# Прописываем в навигационной панели ссылку на поиск.
1. Открываем файл `base.html` или другой шаблон, где находится навигационная панель.
2. Добавляем ссылку на поиск в навигационную панель.
```html
<form class="d-flex" role="search" action="{% url "catalog:search" %}" method="get">
    <input class="form-control me-2" type="search" name="q" placeholder="Search" aria-label="Search">
    <button class="btn btn-outline-success text-white" type="submit">Поиск</button>
</form>
```

# Редактируем форму фильтрации в шаблоне `catalog.html`.
1. Открываем файл `catalog.html` и находим форму фильтров.
- Изменяем форму фильтров, чтобы она отправляла запрос на страницу поиска при наличии параметра `q` в URL.
- {% if request.GET.q %} Если применить фильтры
    - {% url "catalog:search" %} то целевая страница будет поисковая.
- {% else %} Если не применить фильтры
    - {% url "catalog:index" slug_url %} то целевая страница будет каталогом товаров.

```html
<form action="{% if request.GET.q %}{% url "catalog:search" %}{% else %}{% url "catalog:index" slug_url %}{% endif %}" method="get" class="dropdown-menu bg-dark" data-bs-theme="dark">
    </form>
```

- {% if request.GET.q %} Скрытое поле q — сохраняет текущий поисковый запрос при фильтрации
```html
<div>
    {% if request.GET.q %}
        <input type="hidden" name="q" value="{{ request.GET.q }}">
    {% endif %}
</div>
```

# Настраиваем Алгоритм поиска в контроллере.
1. Поиск по ключу `q` из GET запроса
2. Переноси логику в отдельный файл `goods/utils.py` и импортируем его в контроллер.
    - Должен возвращать queryset с отфильтрованными данными.
3. category_slug=None Изменяем значение по умолчанию для выборки.
```python
def catalog(request, category_slug=None):
    query = request.GET.get('q', None) # Поисковый запрос пользователя.

    elif query:
        goods = q_search(query)
```

- Если запрос из цифр и длинна больше 5х символов, то фильтруем по цене.
- filter(id=int(query)) - Применяем метод фильтр чтобы получить (queryset) и преобразуем строку в число.

```python
from goods.models import Products

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
```

## Поиск по ключевым словам с `Q` объект.
- Вызываем специальные `Q` объект для создания сложных запросов с логическими операторами (AND, OR, NOT)
- keywords [] Разбиение запроса на ключевые слова:
    - Разбиваем строку запроса на слова по пробелам
    - Отфильтровываем слова короче 3 символов (слишком короткие для поиска)
- Построение Q-объекта для поиска:
    - Создаём пустой Q-объект
    - Для каждого ключевого слова добавляем условия:
    - `description__icontains` - поиск по описанию (регистронезависимый)
    - `name__icontains` - поиск по названию (регистронезависимый)
    - `|=` означает логическое ИЛИ (OR)

- Возвращаем QuerySet товаров, соответствующих условиям поиска
    - Запрос `"123"` → поиск товара с ID=123
    - Запрос `"стол деревянный"` → поиск товаров, содержащих "стол" ИЛИ "деревянный" в названии ИЛИ описании

```python
from django.db.models import Q

def q_search(query):

    keywords = [word for word in query.split() if len(word) > 2]

    q_objects = Q()
    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)
    return Products.objects.filter(q_objects)
```

# Postgres SQL
https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes

- Переход на другую СУБД (например, PostgreSQL) требует установки соответствующего адаптера и настройки параметров подключения в файле `settings.py`.

- Требует установки psycopg для работы с PostgreSQL.
