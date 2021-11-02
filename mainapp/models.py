from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')     # отображать некие товары первыми
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:  # Проверка на модель
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:

    objects = LatestProductsManager()




class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    # objects = CategoryManager()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    # def get_model_name(self):
    #     return self.__class__.__name__.lower()


class CartProduct(models.Model):
    XS = '39'
    S = '41'
    M = '43'
    L = '45'
    SIZE = (
        (XS, '39'),
        (S, '41'),
        (M, '43'),
        (L, '45'),
    )
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    size = models.CharField(choices=SIZE, default=S, max_length=2, verbose_name='Размер обуви')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    # def save(self, *args, **kwargs):
    #     self.final_price = self.qty * self.content_object.price
    #     super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    # in_order = models.BooleanField(default=False)
    # for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    # orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Winter(Product):
    season = models.CharField(max_length=255, verbose_name='Рекомендуемый сезон для обуви')
    gender = models.CharField(max_length=255, verbose_name='Пол')
    top_material = models.CharField(max_length=255, verbose_name='Материал верха')
    sole_material = models.CharField(max_length=255, verbose_name='Материал подошвы')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Summer(Product):
    season = models.CharField(max_length=255, verbose_name='Рекомендуемый сезон для обуви')
    gender = models.CharField(max_length=255, verbose_name='Пол')
    top_material = models.CharField(max_length=255, verbose_name='Материал верха')
    sole_material = models.CharField(max_length=255, verbose_name='Материал подошвы')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)
