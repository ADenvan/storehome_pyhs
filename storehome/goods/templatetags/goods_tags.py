from django import template
from goods.models import Categories

# Необходимо зарегистрировать теги в шаблоне, чтобы они могли быть использованы в шаблонах.
register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()