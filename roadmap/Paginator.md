
# Pagination in Django
https://docs.djangoproject.com/en/dev/topics/pagination/


# Изменение пагинации на GET запрос
1. через request.GET.get('page', 1) получаем номер страницы из GET запроса. Если параметр не указан, то по умолчанию используется первая страница.
```python
def catalog(request, category_slug):
    page = request.GET.get('page', 1)
    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
```

2. URL адрес открывает с параметром `?page=1` и т.д.
```html
<a class="page-link" href="?page={{page}}">{{ page }}</a>
```


# Filtering Встроенные фильтры.
https://docs.djangoproject.com/en/dev/ref/templates/builtins/

# Настройка формы фильтрации + GET запрос.
1. Прописать URL адрес в форму.
2. Прописали checkbox через GET запрос.
```html
<form action="{% url "catalog:index" slug_url %}" method="get" class="dropdown-menu bg-dark" data-bs-theme="dark">
    <input class="form-check-input" type="checkbox" name="on_sale" id="flexCheckDefault" value="on"
    {% if request.GET.on_sale == 'on' %}checked{% endif %}>
</form>

```

2. В контроллере прописываем (QuerySet) для фильтрации.
- Переменная goods содержит подготовленный набор данных (QuerySet)
    - Фильтр распродаж: Если передан параметр on_sale, выполняется фильтр discount__gt=0 (берутся товары, у которых скидка больше 0).
    - Сортировка: Если передан параметр order_by, список товаров сортируется соответствующим методом.
```python
def catalog(request, category_slug):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)
```

3. Создаем функцию в ШАБЛОННЫХ тегах для постраничной пагинации.

```python
from urllib.parse import urlencode

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
```
- Пример вызова: {% chenge_params page=2 category=5 %}
- Результат: Функция вернет строку вида page=2&category=5&... (все остальные параметры из исходного запроса добавятся автоматически).

- Добавляем шаблонный тег для пагинации и постраничной фильтрации.
```html
{% load goods_tags %}
<a class="page-link" href="?{{ change_params page=page }}">{{ page }}</a>
```
