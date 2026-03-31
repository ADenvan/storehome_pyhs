
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