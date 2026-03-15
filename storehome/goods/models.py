from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    # Class Meta -  Дополнительные параметры модели. Это параметры, которые не влияют на структуру базы данных, но могут влиять на поведение модели.
    class Meta:
        db_table = "category"
        verbose_name = "Категорию"  # Название модели в админке /
        verbose_name_plural = (
            "Категории"  # Название модели во множественном числе в админке
        )

    # Переопределяем метод __str__ для удобства отображения в админке.
    def __str__(self):
        return self.name


# Будет хранить информацию о продуктов.
# Каждый продукт будет иметь название, описание, изображение и цену.
# Также будет ссылка на категорию, в которой находится продукт.
# Это позволит нам легко группировать продукты по категориям.
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"  # Название модели в админке /
        verbose_name_plural = (
            "Продукты"  # Название модели во множественном числе в админке
        )

    def __str__(self):
        return f"{self.name} Количество: {self.quantity}"

    # Присвоить id товару.
    def display_id(self):
        return f"{self.id:05}"

    # Цена продажи с учетом скидки.
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        return self.price