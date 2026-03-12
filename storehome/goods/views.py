from django.shortcuts import render # render - функция для отображения шаблонов




# catalog - страница каталога товаров
def catalog(request):
    return render(request, 'goods/catalog.html')


# Страница товаров 
def product(request):
    return render(request, 'goods/product.html')
