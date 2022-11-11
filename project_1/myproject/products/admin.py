from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Cart, Product, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 

class ProductFrom(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image", "category", "price", "active"]
    search_fields = ['name', 'category__name']
    list_filter = ['name','category__name']
    readonly_fields = ['img']
    form = ProductFrom

    def img(self, products):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='150px'/>".format(img_url=products.image.name, alt=products.name))

    class Media:
        css = {
            'all':('/static/css/style.css',)
        }
        js = ('',)

class ProductAdminSite(admin.AdminSite):
    site_header = 'Hệ thống bán hàng'

admin_site = ProductAdminSite('myProduct')

# admin.site.register(Category)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Cart)
# admin.site.register(Tag)

admin_site.register(Category)
admin_site.register(Product, ProductAdmin)
admin_site.register(Cart)
admin_site.register(Tag)