from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render # render - функция для отображения шаблонов
from goods.models import Products
from goods.utils import q_search

# Контроллер для страницы каталога товаров
# В этом контроллере мы будем получать все товары из базы данных и передавать их в шаблон для отображения.

# Служит обработчиком для URL каталога.
# Принимает объект запроса request и category_slug (идентификатор категории из URL).
def catalog(request, category_slug=None):

    # Получение маршрута через request Делаем ГЕТ запрос
    page = request.GET.get('page', 1) # Получаем номер текущей страницы из параметра запроса 'page'. Если параметр не указан, то по умолчанию используется первая страница.
    on_sale = request.GET.get('on_sale', None) # флаг, указывающий, нужны ли только товары со скидкой.
    order_by = request.GET.get('order_by', None) # поле, по которому необходимо отсортировать товары.
    query = request.GET.get('q', None) # Поисковый запрос пользователя.


    # Выбор товаров ВСЕ или по фильтру из списка.
    if category_slug == 'all': # Если категория равна 'all'
        goods = Products.objects.all() # Получаем все товары из базы данных.
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug)) # Получаем товары из базы данных по категории.

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

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