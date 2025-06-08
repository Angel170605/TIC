from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    stock_img = models.ImageField(upload_to='products', default='profiles/default.png')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='cart', on_delete=models.CASCADE)
    product = models.ManyToManyField('shop.Product', related_name='products', through='shop.CartProduct', blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'Carrito de {self.user.first_name} {self.user.last_name}'
    

class CartProduct(models.Model):
    product = models.ForeignKey('shop.Product', related_name='on_carts', on_delete=models.CASCADE)
    cart = models.ForeignKey('shop.Cart', related_name='cart_products', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    input_text = models.CharField(max_length=250, blank=True, null=True)
    input_image = models.ImageField(upload_to='users_input_images', default='profiles/default.png', blank=True, null=True)

    def __str__(self):
        return self.product.name
