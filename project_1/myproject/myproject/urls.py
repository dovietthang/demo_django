from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('products.urls')),
    path("admin/", admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
