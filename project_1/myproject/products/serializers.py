from rest_framework.serializers import ModelSerializer
from .models import Product, Category, Cart, Tag, User

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','created_at','updated_at','delete_at','active']
     
class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'avatar', 'last_name', 'first_name']

class ProductSerializers(ModelSerializer):
    tags = TagSerializers(many=True)
    category = CategorySerializers()
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price', 'category', 'tags', 'content', 'description', 'created_at', 'updated_at', 'delete_at', 'active']

class CartSerializers(ModelSerializer):
    user = UserSerializers()
    product = ProductSerializers()
    class Meta:
        model = Cart
        fields = ['id', 'product', 'user', 'created_at','updated_at','delete_at','active']
   