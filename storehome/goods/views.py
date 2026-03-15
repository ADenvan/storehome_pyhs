from django.shortcuts import render # render - функция для отображения шаблонов

from goods.models import Products


# catalog - страница каталога товаров
def catalog(request):

    goods = Products.objects.all() # Получаем все товары из базы данных.

    context = {
        "title": "Hme - catalog",
        "goods": goods,  # Передаем переменную goods в шаблон. В шаблоне мы можем обращаться к этой переменной как к списку объектов модели Products. Каждый объект будет представлять собой товар из базы данных. Мы можем использовать цикл for для перебора всех товаров и отображения их на странице каталога.
    }
    return render(request, "goods/catalog.html", context)


# Страница товаров
def product(request):
    return render(request, "goods/product.html")


#