from django.contrib import admin
from django.urls import path

from wbparser.views import index_page, get_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('api/get_products/', get_products),
]
