from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.@
# 1 Product@
# 2 Category
# 3 CartProduct
# 4 Cart
# 5 Order
####################
# 6 Customer
# 7 Specifications

User = get_user_model()


class LatestProductsManager:
    def get_products_for_main_page(self, *args, **kwargs):


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Имя категории', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название продукта')
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена')

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', null=True, on_delete=models.CASCADE,
                             related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Конечная цена')

    def __str__(self):
        return f'Продукт {self.product.title} (для корзины)'


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, verbose_name='Номер')
    adress = models.CharField(max_length=250, verbose_name='Адрес')

    def __str__(self):
        return f'покупатель {self.user.firstname, self.user.lastname}'


class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Дисплей')
    processor_frequency = models.CharField(max_length=9, verbose_name='Частота процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    video = models.CharField(max_length=255, verbose_name='Видеокарта')
    battery_life = models.CharField(max_length=255, verbose_name='Время работы от батареи')

    def __str__(self):
        return f'{self.category.name}:{self.title}'


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Дисплей')
    resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
    accum_volume = models.CharField(max_length=255, verbose_name='Ёмкость аккумулятора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    sd = models.BooleanField(verbose_name='SD карта')
    sd_volume = models.CharField(max_length=255, verbose_name='обЪём SD')
    main_cam_mp = models.CharField(max_length=255, verbose_name='Основная камера')
    front_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная кмера камера')

    def __str__(self):
        return f'{self.category.name}:{self.title}'
