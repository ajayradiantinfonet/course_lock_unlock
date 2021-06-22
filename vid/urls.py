from django.contrib import admin
from django.urls import path
from .views import index,premimum

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('premimum<int:id>/', premimum, name='premimum'),
]
