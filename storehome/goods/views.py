from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render # render - функция для отображения шаблонов
from goods.models import Products

# Контроллер для страницы каталога товаров
# В этом контроллере мы будем получать все товары из базы данных и передавать их в шаблон для отображения.

# catalog - страница каталога товаров
def catalog(request, category_slug):

    # Получение маршрута через request Делаем ГЕТ запрос
    page = request.GET.get('page', 1) # Получаем номер текущей страницы из параметра запроса 'page'. Если параметр не указан, то по умолчанию используется первая страница.

    # Выбор товаров ВСЕ или по фильтру из списка.
    if category_slug == 'all': # Если категория равна 'all'
        goods = Products.objects.all() # Получаем все товары из базы данных.
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) # Получаем товары из базы данных по категории.


    paginator = Paginator(goods, 3)  # Создаем объект Paginator, который будет разбивать список товаров на страницы. Каждая страница будет содержать 3 товара.
    current_page = paginator.page(int(page)) 


    context = {
        "title": "Hme - catalog",
        "goods": current_page,
        "slug_url": category_slug,


    }
    return render(request, "goods/catalog.html", context)


# Страница товаров
def product(request, product_slug):
    product = Products.objects.get(slug=product_slug) # Получаем товар по его ID из базы данных.

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)


#