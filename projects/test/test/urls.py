from django.contrib import admin
from django.urls import path
from calc import views
from django.urls import include

urlpatterns = [
    path('calc/', include('calc.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
