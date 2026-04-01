from django import template
from django.utils.http import urlencode

from goods.models import Categories

# Необходимо зарегистрировать теги в шаблоне, чтобы они могли быть использованы в шаблонах.
register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# указывает, что это простой тег, который принимает контекст Django как первый аргумент (где хранится request).
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """ Функция принимает словарь всех параметров из GET запроса
        (context['request'].GET.dict()) и дополняет его любыми дополнительными аргументами, переданными в теге (**kwargs).
        return urlencode(query) — возвращает итоговую строку параметров, закодированную для адреса (например, param=value&other=123).
    """
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)