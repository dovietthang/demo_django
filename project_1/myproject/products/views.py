from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product, Cart, Category, Tag 
from .serializers import ProductSerializers, CartSerializers, TagSerializers, CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticated]
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAuthenticated]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.filter(active=True)
    serializer_class = CartSerializers
    permission_classes = [permissions.IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(active=True)
    serializer_class = TagSerializers
    permission_classes = [permissions.IsAuthenticated]


# def index(request):
#     return render(request, template_name='index.html', context={
#         'name':'Products'
#     })
