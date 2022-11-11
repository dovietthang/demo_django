from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('products.urls')),
    # path("admin/", admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
