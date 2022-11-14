from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from .admin import admin_site

router = DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('cart', views.CartViewSet)
router.register('tag', views.TagViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # path('admin/', admin_site.urls),
]