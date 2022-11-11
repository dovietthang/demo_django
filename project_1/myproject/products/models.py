from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class ItemBase(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class User(AbstractUser):
    class Meta:
        db_table = 'users'

    avatar = models.ImageField(upload_to='upload/%y/%m', default=None)

class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Product(ItemBase):
    class Meta:
        # unique_together = ('name', 'category')
        db_table = 'products'

    def __str__(self):
        return self.name
        
    name = models.CharField(max_length=255, null=False, unique=True)
    price = models.CharField(max_length=100, null=False, default=None)
    description = RichTextField(null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True, default=None)
    image = models.ImageField(upload_to='product/%y/%m', default=None)

class Cart(ItemBase):
    class Meta:
        # unique_together = ('name', 'product')
        db_table = 'carts'
    
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Tag(models.Model):
    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True, default=None)
