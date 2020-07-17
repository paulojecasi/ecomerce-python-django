from django.contrib import admin
from django.urls import path, include
from .views import hello_world
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('pedidos/', include('sitepedidos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),








  #  path('pedidos/', stpedidos),
  #  path('bebidas/',pedBebidas,name="pedBebidas"),
  #  path('aluguel/',pedAluguel),
  #  path('sobre/',sobreoSite),

   # path('clientes/', include('cliente.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)